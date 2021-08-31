#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if y is not x[1]:
    print(f'expression is true: {y}')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))