from xml.dom.minidom import parse
from xml.sax.saxutils import XMLFilterBase, XMLGenerator
import xml.dom.minidom
import xml.sax


class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self.line = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""
        self.publish_date = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.currentTag = tag
        if tag == "book":
            print("\n*****\tBook\t*****\n")
            title = attributes["id"]
            print("Title:", title)

    def endElement(self, tag):
        if tag == "author":
            print("Author:", self.author)
        elif tag == "title":
            print("Title:", self.title)
        elif tag == "genre":
            print("Genre:", self.genre)
        elif tag == "price":
            print("Price:", self.price)
        elif tag == "publish_date":
            print("Publish date:", self.publish_date)
        elif tag == "description":
            print("Description:", self.description)
            self.description = ''

        self.currentTag = ''

    def characters(self, content):
        self._charBuffer.append(content)
        if self.currentTag == "author":
            self.author = content
        elif self.currentTag == "title":
            self.title = content
        elif self.currentTag == "genre":
            self.genre = content
        elif self.currentTag == "price":
            self.price = content
        elif self.currentTag == "publish_date":
            self.publish_date = content
        elif self.currentTag == "description":
            self.description += content


class Modify(XMLFilterBase):
    def __init__(self, id, tagToEdit, text, parent=None):
        super().__init__(parent)
        self.id = id
        self.tagToEdit = tagToEdit
        self.text = text
        self.isThatElement = 0
        self.isThatTag = 0

    def editThis(self):
        return self.isThatElement == 1 and self.isThatTag == 1

    def startElement(self, tag, attributes):
        if tag == "book" and attributes["id"] == self.id:
            self.isThatElement += 1
        if tag == self.tagToEdit:
            self.isThatTag += 1

        super().startElement(tag, attributes)

    def endElement(self, tag):
        if tag == "book" and self.isThatElement == 1:
            self.isThatElement -= 1
        if tag == self.tagToEdit:
            self.isThatTag -= 1

        super().endElement(tag)

    def characters(self, content):
        if self.editThis():
            super().characters(self.text)
        else:
            super().characters(content)


def testSax(file):
    HandlerToPrint = MyHandler()
    viewer = xml.sax.make_parser()
    viewer.setContentHandler(HandlerToPrint)
    viewer.parse(file)

    writer = Modify('bk107', 'author', 'Sebix', viewer)

    with open('edited.xml', 'w') as f:
        handlerToEdit = XMLGenerator(f)
        writer.setContentHandler(handlerToEdit)
        writer.parse(file)


def testDOM(file):
    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print("Root element : %s" % collection.getAttribute("shelf"))

    books = collection.getElementsByTagName("book")

    for book in books:
        print("\n*****\tBook\t*****\n")
        author = book.getElementsByTagName('author')[0]
        print("Author: %s" % author.childNodes[0].data)
        title = book.getElementsByTagName('title')[0]
        print("Title: %s" % title.childNodes[0].data)
        genre = book.getElementsByTagName('genre')[0]
        print("Genre: %s" % genre.childNodes[0].data)
        price = book.getElementsByTagName('price')[0]
        print("Price: %s" % price.childNodes[0].data)
        publish_date = book.getElementsByTagName('publish_date')[0]
        print("Publish date: %s" % publish_date.childNodes[0].data)
        description = book.getElementsByTagName('description')[0]
        print("Description: %s" % description.childNodes[0].data)

def main():
    file = input("Give me file: ")
    print("====================   SAX   ====================\n")
    testSax(file)
    print("\n\n====================   DOM   ====================\n")
    testDOM(file)


if __name__ == "__main__":
    main()
