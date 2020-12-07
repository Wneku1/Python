import csv
import os
import time


class CsvEditor:
    def __init__(self, file):
        self.file = file
        self.dict = self.getDictFromCsv()

    def getDictFromCsv(self):
        with open(self.file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            id = 0
            toRet = {}
            for row in csv_reader:
                id += 1
                toRet[id] = {}
                toRet[id]['Brand'] = row['Brand']
                toRet[id]['Model'] = row['Model']
                toRet[id]['Engine'] = row['Engine']
                toRet[id]['Year'] = row['Year']
            return toRet

    def saveDictToCsv(self):
        with open(self.file, mode='w') as csv_file:
            fieldnames = ['Brand', 'Model', 'Engine', 'Year']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for element in self.dict:
                writer.writerow({'Brand': self.dict[element]["Brand"],
                                 'Model': self.dict[element]["Model"],
                                 'Engine': self.dict[element]["Engine"],
                                 'Year': self.dict[element]["Year"]})

    def drawDict(self):
        for x in range(10):
            print('\x1b[2J')  # if is not terminal
        os.system('clear')  # only in terminal
        fieldnames = ['Brand', 'Model', 'Engine', 'Year']
        col_width = max(len(self.dict[i][f]) for i in self.dict for f in fieldnames) + 2
        for word in fieldnames:
            if word == 'Brand':
                print('ID'.ljust(col_width), end='')
                print((str(word)).ljust(col_width), end='')
            elif word == 'Year':
                print((str(word)).ljust(col_width))
            else:
                print((str(word)).ljust(col_width), end='')

        for i in self.dict:
            print((str(i)).ljust(col_width), end='')
            for key in fieldnames:
                if key == 'Year':
                    print((self.dict[i][key]).ljust(col_width))
                else:
                    print((self.dict[i][key]).ljust(col_width), end='')

    def addNew(self, brand, model, engine, year):
        newKey = 1
        while newKey in self.dict:
            newKey += 1
        self.dict[newKey] = {}
        self.dict[newKey]['Brand'] = brand
        self.dict[newKey]['Model'] = model
        self.dict[newKey]['Engine'] = engine
        self.dict[newKey]['Year'] = year
        self.saveDictToCsv()

    def delRow(self, whichOne):
        if whichOne in self.dict:
            del self.dict[whichOne]
            self.saveDictToCsv()
        else:
            print("That ID doesn't exist\n")

    def navigation(self):
        while True:
            options = ['1. Add record', '2. Delete record', '3. Quit']
            self.drawDict()
            print('\n')
            for opt in options:
                print(opt)
            print('\n')
            choice = input('Enter choice: ')

            if choice == '1':
                newRecord = input('Enter: Brand, Model, Engine, Year \n')
                splited = newRecord.split(',')
                self.addNew(splited[0], splited[1], splited[2], splited[3])
                print("Your record has been added\n")
                time.sleep(1)
            elif choice == '2':
                whichOne = input('Enter which ID remove: \n')
                self.delRow(int(whichOne))
                print("Your record has been deleted\n")
                time.sleep(1)
            elif choice == '3':
                return


def test():
    testEditor = CsvEditor("cars.csv")
    testEditor.navigation()

if __name__ == "__main__":
    test("cars.csv")
