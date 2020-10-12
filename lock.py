import os


def clearTerminal():
    os.system('clear')  # only in terminal 


passwd = input("Set password ")

clearTerminal()

isCorrect = False;

while not isCorrect:
    tempPasswd = input("Enter password ")
    isCorrect = tempPasswd == passwd
    if not isCorrect:
        print("Try again.")
    else:
        print("Correct")
