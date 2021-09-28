#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
"""
def f1(f):
    def f2():
        print('this is before function call')
        f()
        print('this is after function call')

    return f2


@f1
def f3():
    print("this is f3")


f3()


def F1(f):
    print('A')
    def F2():
        print('B')
        f()
        print('C')
    print('D')
    return F2
@F1
def F3():
    print('E')
F3()
"""


def generator(start, stop):
    while start <= stop:
        yield start
        print(f'start={start}')
        start += 1


for counter in generator(3, 4):
    print(f'counter={counter}')
