# monday_temperatures = [9.1, 8.8, 7.5]

# student_grades = {"marry":9.1, "JP":8.8, "John":7.5}

# mysum = sum(student_grades.values())
# length = len(student_grades)
# print(mysum/len(student_grades))

# print(type(student_grades))
"""
def mean(mylist):
    the_mean = sum(mylist)/len(mylist)
    return the_mean


print(mean([1, 4, 5]))
"""

#  monday_temperatures = [9.1, 8.8, 7.5]
#
#  for temp in monday_temperatures:
#     print(round(temp))

#
# for letter in 'Hello':
#     print(letter.title())

# student_grades = {"marry": 9.1, "JP": 8.8, "John": 7.5}
#
# for grades in student_grades.values():
#     print(grades)
#
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
#
# for key, value in phone_numbers.items():
#     print(f"{key} has as phone number {value}")
#
#
# username = ''
#
# while username != 'pypy':
#     username = input("Enter username: ")
#
# temps = [221, 234, 340, 230, -9999]
#
# new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]
# print(new_temps)

#
# def mean(**kwargs):
#     return kwargs
#
#
# print(mean(a=1, b=3, c=3, d=4))

#
# with open('../utils/fruits.txt', 'a+') as file:
#     file.write("\n Okra")
#     file.seek(0)
#     con = file.read()
#
# print(con)
#
import os
import time
import pandas

while True:
    if os.path.exists("../utils/temp_today.csv"):
        data2 = pandas.read_csv("../utils/temp_today.csv")
        print(data2.mean()["st1"])

    else:
        print("File does not exist")

    time.sleep(3)

