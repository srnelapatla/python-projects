# this is the example of csv file reader

import csv

with open(r'C:\000_Development\pythonFiles\example1.csv') as csvFile:
    csv_record = csv.reader(csvFile, delimiter=',')

    headerRec = 0
    for row in csv_record:
        headerRec +=1
        if headerRec == 1:
            print(f'{",".join(row)}')
        else:
            print(f'{"--->".join(row)}')
        #print(row)
