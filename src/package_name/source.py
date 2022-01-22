#!/bin/env python

def hi(a, b):
    # intentional pep8 violations to make flake8 say things. (too many blank lines)
    return a > b


# intentional mypy error
# def staticlytyped(a: int, b: int) -> bool:
#    return a + b


def main():
    return 0


if __name__ == '__main__':
    main()
