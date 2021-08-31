#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack'
    walking = 'Walking like a duck'

    def quack(self) -> None:
        print(self.sound)

    def walk(self) -> None:
        print(self.walking)


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == '__main__':
    main()
