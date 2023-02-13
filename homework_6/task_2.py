import math


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    x1 = 0
    x2 = 0
    # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
    if d > 0:
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
    elif d == 0:
        x = -b / (2 * a)
    else:
        print('x1 is None')
        print('x2 is None')
    return x1, x2


a, b, c = map(float, input('введи три числа: ').split())