import os.path


def fileCounter():
    DIR = 'dev'
    numberFiles = 0
    for name in os.listdir(DIR):
        if os.path.isfile(os.path.join(DIR, name)):
            numberFiles += 1

    print("Number files in " + str(DIR) + ": " + str(numberFiles))


if __name__ == "__main__":
    fileCounter()