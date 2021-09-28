'''
Python script for Budget analysis final project
-- "Jeyaprakash Dasu Rajagopal"
'''


import locale
import pandas as pd

locale.setlocale(locale.LC_ALL, '')
csv_file = 'city-of-seattle-2012-expenditures-dollars.csv'
data = pd.read_csv(csv_file, sep=',', index_col="Department").fillna(value=0)
data2 = pd.read_csv(csv_file)
data2 = data2.iloc[:-1, :]
dept = data2.Department.unique()

print("Department        Total")

for col in dept:
    amount = data.loc[col, "2012 Actual"]
    total = locale.currency(amount.sum(), grouping=True)

    print("%s   " % col, total)
    