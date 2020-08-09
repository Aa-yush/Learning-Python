import pandas as pd

file = pd.ExcelFile('readFile.xlsx')
print(file.sheet_names)

sheet = file.parse('sales')
print(sheet)

print(sheet.date)

print(sheet.amount.sum())

print(sheet.loc[0])

print(sheet.loc[0,'amount'])

print(sheet.loc[sheet['amount']==7999])

print(sheet.loc[sheet['amount']>5000])

print(sheet.loc[sheet['amount'].idxmax()])

print(sheet.loc[sheet['amount'].idxmax()]['date'])
