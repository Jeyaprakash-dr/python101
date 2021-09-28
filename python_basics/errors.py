def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You are dividing by zero or is meaningless")


print(divide(10, 5))
print("End of Program")

