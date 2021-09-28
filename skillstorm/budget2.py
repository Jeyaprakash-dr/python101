import csv


class Expenses:
    dept_name: str
    expense_amount: float

    def __init__(self, dept_name, expense):
        self.dept_name = dept_name
        self.expense = expense


with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    reader = csv.reader(file, delimiter=",")
    expense_list = []
    row_number = 1

    for line in reader:
        if row_number != 1:
            expense_amount = Expenses(line[0], line[3])
            expense_list.append(expense_amount)
            row_number += 1
        else:
            row_number += 1

expense_dict = {}

for item in expense_list:
    # if the key is not in the dictionary, 1st occurrence of the dept
    if not(item.dept_name in expense_dict):
        expense_dict[item.dept_name] = [item.expense_amount]
    else:
        expenses = expense_dict[item.dept_name]
        expenses.append(item.expense_amount)
        expense_dict[item.dept_name] = expenses

print(expense_dict)

# key - dept_name, list of expenses - values

