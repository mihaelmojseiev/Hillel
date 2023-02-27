import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d > r1 + r2 or d < r2 - r1 or d < r1 - r2


def main():
    x1, y1, r1, x2, y2, r2 = map(int, input("Введи 6 значений: ").split())

    print(circles_intersect(x1, y1, r1, x2, y2, r2))


if __name__ == "__main__":
    main()