#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    first = (-b + math.sqrt(d)) / (2*a)
    second = (-b - math.sqrt(d)) / (2*a)
    return (first, second)


def main():
    pass


if __name__ == "__main__":
    main()
