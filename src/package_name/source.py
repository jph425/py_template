#!/bin/env python

def hi(a, b):
    # delete lines 5-10 to create a flake8 error.
    #   line  5
    #   line  6
    #   line  7
    #   line  8
    #   line  9
    #   line 10
    return a > b


# intentional mypy error
# def staticlytyped(a: int, b: int) -> bool:
#     return a + b


def main():
    return 0


if __name__ == '__main__':
    main()
