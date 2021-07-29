# Conditions
'''
marks = float(input("Enter the students grade: "))

if marks >= 90:
    print("Congratulations its Grade A")
elif marks >=80 and marks <=89:
    print("Congratulations its Grade B")
elif marks >=70 and marks <=79:
    print("Congratulations its Grade C")
elif marks >=60 and marks <=69:
    print("Congratulations its Grade D")
elif marks <=59:
    print("Congratulations its Grade F")


import sys
print ("Python version " + str(sys.version))
print("Version info " )
print (sys.version_info)

import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))



Circum = float(input("Enter the circumference value: "))
Radius = Circum/(2*3.14)
print("Radius of the circle: " + str(Radius))

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print("Your name is " + lname +","+ fname)

# For loop : iteration numbers are well known
word = ""
for num in range(5, 10):
    word = word + "*"

print(word)


# While loop: number of iterations are not knows

number = 2000

# exit condition
while number > 1000:
    number = number * 2
    if number > 10000000:
        break # 1 iteration of the loop # break will break entire iteration of the loop
    print(number)
print("Finished")



# List in python
# [] mean we are gonna create list,
# Lists: storing multiple related values in same variable
weekly_temp = [45, 67, 90, 45, 75, 80]
# index:        0,  1  2   3  4     5
# slicing the list
print(weekly_temp[2:])
print(weekly_temp)

weekly_temp[2] = 60
print(weekly_temp)

for temp in weekly_temp:
    temp = int((temp - 32) * (5/9))
    print("Temp in Celcius: " + str(temp))

groceries = ["milk", "eggs", "bread", "butter", "bacon"]
groceries.append("yogurt")
#print(groceries.count(4))
print(groceries)
groceries.reverse()
print(groceries)
groceries.sort()
print(groceries)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

# import collections
from collections import deque
queue = deque(["JP", "Vishnu", "Kave"])
queue.append("Jitesh")
queue.append("Bob")
print(queue.popleft())
print(queue.popleft())
print(queue)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

squares3 = [x**2 for x in range(10)]
print(squares3)


# python code to draw an object
print("   /|")
print("  / |")
print(" /  |")
print("/___| ")


combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

vec = [-4,-2,0,2,4]
print([abs(x) for x in vec])

groceries = ["milk", "eggs", "bread", "butter", "bacon"]
x = []
for x in groceries:
    x = (x + "ay")

print(x)

x = [(x + "ay") for x in groceries]
print(x)

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(matrix)
out = [[row[i] for row in matrix ] for i in range(4)]
print(out)

# tuple : immutable list
lotto_numbers = (32,35,76,2,20)
#lotto_numbers[2] = 90
print(lotto_numbers)

my_list = ["JP, Vishnu, Jitesh, Kave"]
my_tuple = tuple(my_list)
print(my_tuple)

# Dictionary storing key value pairs (entries)

user_dictionary = {
    "JP": "984047104",
    "VP": "9790705116"
}

search = input("Search by the user name: ")
print(user_dictionary[search])


user_mail = {
    "JP": "jeyaprakash.dr@gmail.com",
    "VP": "priya2prakash@gmail.com"
}

#search = input("Search email by entering the person name: ")
#print("The email id of the user is " + user_mail[search])



dict = {
    "Hello": "Python"
}
print(dict.get("Hello"))
#print(dict[0])
print(dict["Hello"])

x = 5
if not(x > 0):
    print("Hello Python")
else:
    print("Hello World")




# defining a function
# def function_name ():
def say_hello():
    print("Hello")
    print("Hello Python")


# calling a function
say_hello()


# Parameters
def add(num1, num2):
    return num1 + num2


# arguments are being passwe
solution2 = add(2, 4)
print(solution2)

print(add("Hello", "World"))

x = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(x)):
    print(i, x[i])

print(sum(range(4)))
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, )
        



#import pandas
#dataframe = pandas.read_csv('vms.csv')
#print(dataframe)


import numpy as np
a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)


# define the state and behaviour of particular object
class Product:
    # data, state related to particular product
    price: float
    name: str
    is_active: bool

    # behaviour
    def set_price(self, price):
        # data validation
        if price < 0:
            self.price = 0
        self.price = price

    def get_price(self):
        return self.price

    # constructor: initial values for the object
    def __init__(self, name, price, is_active):
        self.name = name
        self.price = price
        self.is_active = is_active


tv = Product("TV", 500, True)
#fridge = Product()




# create an object using the class
product = Product()
product.name = 'TV'

product2 = Product()
product2.name = 'Fridge'
print(product2.name)


class Developer:
    def code(self):
        print("My first class object exampled")


object = Developer()
object.code()




class Person:
    name: str
    email: str
    id: int


class Developer:

    name: str
    sware: str
    balance: int

    def info(self):
        print("Information ")

    def __init__(self, name, sware, balance):
        self.name = name
        self.sware = sware
        self.balance = balance


object = Developer("Jeyaprakash", "python", 100000)
object1 = Developer("vishnupriya", "sql", 1000000)
print(object.name + " " + object.sware)




# Parent Class
class Animal:
    weight: int
    name: str

    def speak(self):
        return "Strange nosie"


# Dog extends the class animal
class Dog(Animal):
    breed: str

    def play(self):
        print("Playing")

    # Overwriting method
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


list = [Dog(), Cat(), Dog(), Animal()]
for animal in list:
    print(animal.speak())
    

from pydantic import BaseModel


class Person(BaseModel):
    id: int
    name: str


customer = {
    "id": 1,
    "name": "JP"
}


# unpacking
p = Person(**customer)
print(str(p.id) + " : " + p.name)



class Person:
    name: str
    email: str
    id: int


class Developer:

    name: str
    sware: str
    balance: int

    def info(self):
        print("Information ")

    def __init__(self, name, sware, balance):
        self.name = name
        self.sware = sware
        self.balance = balance


object = Developer("Jeyaprakash", "python", 100000)
object1 = Developer("vishnupriya", "sql", 1000000)
print(object.name + " " + object.sware)



file = open("users.txt", "r")
for line in file:
    print(line)

file.close()
'''


with open("numbers.txt", "r") as file:
    for line in file:
        print(line)

print(file.closed)

total = 0
with open("numbers.txt", "r") as file:
#for line in file:
#    for char in line:
#        if char.isdigit():
#            total = total + int(char)
    total = [(total + int(char)) for line in file for char in line if char.isdigit()]

print(total)

