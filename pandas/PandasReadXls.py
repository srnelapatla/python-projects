import pandas as pd

# import openpyxl
# now read excel file
dfile = '/Users/srnelapatla/000_development/PythonDataFiles/SampleData.xlsx'
xlsFile = pd.read_excel(dfile, sheet_name='SalesOrders')

# all columns;
print(xlsFile)
# to get particular columns
print(xlsFile[['Item', 'Unit Cost']])

#get items cost more than $5
newDataFrame = xlsFile[xlsFile['Unit Cost'] > 5.00]
print(newDataFrame[['Region', 'Item', 'Unit Cost']])
