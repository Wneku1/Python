def inputName():
    dataIn = input("Enter your name, surname and year of birth: \n")
    dataList = dataIn.split()
    print("Your name is: " + dataList[0])
    print("Your surname is: " + dataList[1])
    print("Your year of birth is: " + dataList[2])


if __name__ == "__main__":
    inputName()
