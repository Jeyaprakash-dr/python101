#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print('Meow.')
    return dict(x=42, y=42, z=44)

for letter in 'abc':
    print(letter.upper())

if __name__ == '__main__':
    main()
