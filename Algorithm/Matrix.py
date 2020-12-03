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


def testAdding():
    m1 = Matrix([[1, 2, 3],
                 [4, 5, 6]])

    m2 = Matrix([[7, 8, 9],
                 [10, 11, 12]])
    m3 = m1 + m2
    m3.draw()


testAdding()
