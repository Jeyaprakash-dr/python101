#
# Example file for working with classes
#

import file_two

print("File one __name__ is set to: {}" .format(__name__))


class myclass():
    def method1(self):
        print("My calss method1")

    def method2(self, someString):
        print("mycalss method2 " + someString)

class anotherclass(myclass):
    def method1(self):
        myclass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ")


def main():
    c = myclass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherclass()
    c2.method1()
    c2.method2("This is a string ")

if __name__ == "__main__":
    main()
