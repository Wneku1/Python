from multiprocessing.pool import Pool
from Python.Algorithm.Matrix import Matrix
import matplotlib.pyplot as plt
import random as rn


def doSomeCalculation(size):
    print("Started on matrix in size: ", size)
    m1 = Matrix([[rn.randint(1, 10) for i in range(size)] for i in range(size)])
    return m1.calcDeterminant() % 100000


if __name__ == "__main__":
    p = Pool(processes=4)

    sizes = [2, 4, 6, 8, 10, 12, 14]
    finList = []

    result = p.map(doSomeCalculation, sizes)
    p.close()
    p.join()

    plt.hist(result, bins=16)
    plt.show()

    print('Result: \n {0}'.format(result))
