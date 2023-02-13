import math


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    sqrtr = math.sqrt(abs(d))
    if d > 0:
        x1 = (-b + sqrtr) / 2 * a
        x2 = (-b - sqrtr) / 2 * a
        print(x1, x2)
    elif d == 0:
        x3 = -b / (2 * a)
        print(x3)
        print(None)
    else:
        print('x1 is None')
        print('x2 is None')


a, b, c = map(float, input('введи три числа: ').split())

if a == 0:
    print("Неправильно а ввёл, повтори")

else:
    solve_quadratic_equation(a, b, c)