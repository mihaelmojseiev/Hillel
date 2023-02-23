import math


def solve_quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    sqrtr = d**0.5
    x1 = (-b + sqrtr) / (2 * a)
    x2 = (-b - sqrtr) / (2 * a)
    return x1, x2


def main():
    a, b, c = map(float, input("введи три числа: ").split())

    if a == 0:
        print("Неправильно а ввёл, повтори")

    else:
        print(solve_quadratic_equation(a, b, c))


if __name__ == "__main__":
    main()
