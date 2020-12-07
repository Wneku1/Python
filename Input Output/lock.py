import os


def clearTerminal():
    for x in range(10):
        print('\x1b[2J')  # if is not terminal
    os.system('clear')  # only in terminal


def lock():
    passwd = input("Set password: \n")
    clearTerminal()
    isCorrect = False
    while not isCorrect:
        tempPasswd = input("Enter password ")
        isCorrect = tempPasswd == passwd
        if not isCorrect:
            print("Try again.")
        else:
            print("Correct")


if __name__ == "__main__":
    lock()
