import os.path

# path joining version for other paths
DIR = 'dev'
# numberFiles =  for name in os.listdir(DIR):
#                             if os.path.isfile(os.path.join(DIR, name))

numberFiles = 0
for name in os.listdir(DIR):
    if os.path.isfile(os.path.join(DIR, name)):
        numberFiles += 1

print("Number files in " + str(DIR) + ": " + str(numberFiles))
