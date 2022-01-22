#!/bin/env python

def hi(a, b):
    return a > b


# intentional mypy error
# def staticlytyped(a: int, b: int) -> bool:
#    return a + b


def main():
    return 0


if __name__ == '__main__':
    main()
