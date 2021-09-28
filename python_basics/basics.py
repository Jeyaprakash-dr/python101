"""
def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


student_grades = {"marry": 9.1, "JP": 8.8, "John": 7.5}
print(student_grades.values())
print(mean(student_grades))

monday_temperatures = [9.1, 8.8, 10.5]
print(mean(monday_temperatures) * 20)
"""
#
#
# def weather_condition(temperature):
#     if temperature > 7:
#         return "warm"
#     else:
#         return 'Cold'
#
#
# print(weather_condition(float(input("Enter Temperature: "))))
#
# name = input("Enter your name: ")
# surname = input("Enter surname: ")
# message = "Hello %s %s" % (name, surname)
# message2 = f"Hello {name}, {surname}!"
# print(message


while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue
