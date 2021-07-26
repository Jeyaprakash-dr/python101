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

'''

import sys
print ("Python version " + str(sys.version))
print("Version info " )
print (sys.version_info)

import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

'''

Circum = float(input("Enter the circumference value: "))
Radius = Circum/(2*3.14)
print("Radius of the circle: " + str(Radius))

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print("Your name is " + lname +","+ fname)
'''
