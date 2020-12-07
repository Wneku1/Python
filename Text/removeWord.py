from typing import Tuple


def removeWord():
    wordToRemove: Tuple[str, str, str, str] = ("się", "i", "oraz", "nigdy")
    temporaryText = []
    file = input("Give me file: ")

    with open(file, 'r', encoding='utf8') as fin:
        for line in fin:
            for word in wordToRemove:
                line = line.replace(("{} ".format(word)), "")
                line = line.replace((" {} ".format(word)), "")
                line = line.replace(" {}".format(word), "")
            temporaryText.append(line)

    with open(file, 'w+') as fout:
        for line in temporaryText:
            fout.write(line)


if __name__ == "__main__":
    removeWord()
