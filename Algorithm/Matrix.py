import random as rn
from typing import List


class Matrix:
    def __init__(self, data) -> object:
        self.data = data

    def draw(self):
        lengthRows = len(self.data)
        lengthColumns = len(self.data[0])
        for lr in range(lengthRows):
            print('|', end=' ')
            for lc in range(lengthColumns):
                print(''.join('{0}'.format(self.data[lr][lc])), end=' ')
            print('|')
        print('\n')

    def size(self):
        return len(self.data), len(self.data[0])

    def __getitem__(self, row):
        return self.data[row]

    def zeros(self, rows, columns):
        listZero = []
        matrix: List[List[int]] = []
        for i in range(columns):
            listZero.append(0)
        for j in range(rows):
            matrix.append(listZero)
        self.data = matrix

    def __add__(self, other):
        if self.size() != other.size():
            raise Exception("The matrices must be of the same size")

        lRows1 = len(self.data)
        lCol1 = len(self.data[0])

        data = []
        for lr in range(lRows1):
            temp = []
            for lc in range(lCol1):
                temp.append(self.data[lr][lc] + other.data[lr][lc])
            data.append(temp)
        return Matrix(data)

    def __mul__(self, other):

        otherRow, otherCol = other.size()
        selRow, selCol = self.size()

        if selCol != otherRow:
            raise Exception("Wrong matrices size")

        lRows1 = len(self.data)
        lCol1 = len(self.data[0])
        lCol2 = len(other.data[0])

        data = []
        for i in range(lRows1):
            temp = []
            for j in range(lCol2):
                s = 0
                for k in range(lCol1):
                    s += self.data[i][k] * other.data[k][j]
                temp.append(s)
            data.append(temp)

        return Matrix(data)


def testAdding(printResult):
    m1 = Matrix([[rn.randint(1, 100) for i in range(128)] for i in range(128)])
    m2 = Matrix([[rn.randint(1, 100) for i in range(128)] for i in range(128)])
    m3 = m1 + m2
    if printResult:
        m1.draw()
        m2.draw()
        m3.draw()


def testMultiple(printResult):
    m1 = Matrix([[rn.randint(1, 100) for i in range(8)] for i in range(8)])
    m2 = Matrix([[rn.randint(1, 100) for i in range(8)] for i in range(8)])
    m3 = m1 * m2
    if printResult:
        m1.draw()
        m2.draw()
        m3.draw()


testAdding(False)
testMultiple(False)
