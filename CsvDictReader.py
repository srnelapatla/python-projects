import csv

with open('C:\\000_Development\\pythonFiles\\csvDictReader.txt', mode='r') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        #print(row)
        print(f'\t{row["name"]} works at {row["department"]} and his birth day in {row["birthdayMonth"]}')