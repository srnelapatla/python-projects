# simple file reader example

# file1 = open("C:\\000_Development\\pythonFiles\\csvDictReader.txt")

# for fl in file1:
#    print(fl)

with open('C:\\000_Development\\pythonFiles\\csvDictReader.txt', mode='r') as file1:
    fileReader = file1.read()
   # print(fileReader)

with open('C:\\000_Development\\pythonFiles\\csvDictReader2.txt', mode='w') as file2:
    file2.write(fileReader)
