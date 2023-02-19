import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if d>r1 + r2:
        return d>r1 + r2
    elif d<r2 - r1:
        return d<r2 - r1
    else:
        return d==r2 - r1


def main():
    x1, y1, r1, x2, y2, r2 = map(int, input("Введи 6 значений: ").split())

    print(circles_intersect(x1, y1, r1, x2, y2, r2))


if __name__ == '__main__':
    main()