import random


def partition(array, begin, end):
    pivot = array[begin]
    l: [int] = begin + 1
    r: [int] = end - 1

    while True:

        while l <= r and array[r] >= pivot:
            r = r - 1

        while l <= r and array[l] <= pivot:
            l = l + 1

        if l <= r:
            array[l], array[r] = array[r], array[l]
        else:
            break

    array[begin], array[r] = array[r], array[begin]

    return int(r)


def MyQuickSort(array, begin, end):
    if begin >= end:
        return

    p = partition(array, begin, end)
    MyQuickSort(array, begin, p)
    MyQuickSort(array, p + 1, end)


def testAndCompare():
    test1 = random.sample(range(0, 1000), 50)
    testBi = test1.copy()
    n = len(test1)
    MyQuickSort(test1, 0, n)
    testBi.sort()
    print(test1)
    print(testBi)

    if test1 == testBi:
        print("OK")
    else:
        print("Not OK")


if __name__ == "__main__":
    testAndCompare()
