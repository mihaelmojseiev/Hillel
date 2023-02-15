def sign(x):
    if x > 0:
        res = 1
        return res
    elif x < 0:
        res = -1
        return res
    elif x == 0:
        res = 0
        return res


def main():
    x = int(input('Введи x: '))
    print(sign(x))


if __name__ == '__main__':
    main()