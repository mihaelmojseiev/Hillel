import math


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    sqrtr = math.sqrt(abs(d))
    if d > 0:
        x1 = (-b + sqrtr) / 2 * a
        x2 = (-b - sqrtr) / 2 * a
        return x1, x2

    elif d == 0:
        x3 = -b / 2 * a
        return x3, None

    else:
        return None


def main():
    a, b, c = map(float, input('введи три числа: ').split())
    print(solve_quadratic_equation(a, b, c))


if __name__ == '__main__':
    main()