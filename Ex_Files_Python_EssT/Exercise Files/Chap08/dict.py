#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
              'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    print('found' if 'lioness' in animals else 'nope')
    animals['monkey'] = "I am monkey hahaha"
    print(animals.get('godzilla'))
    print_dict(animals)


def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')


if __name__ == '__main__': main()
