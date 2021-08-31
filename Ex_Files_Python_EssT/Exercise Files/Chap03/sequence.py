#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}


x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(id(x))
print(id(y))

if isinstance(y, tuple):
    print("yep")
elif isinstance(y, list):
    print("yep its a list")
else:
    print("nope")
#for k, v in x.items():
#    print('k: {}, v: {}'.format(k, v))
