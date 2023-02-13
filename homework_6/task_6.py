x = int(input('Введи x: '))


def sign(x):
    if x > 0:
        res = 1
        print(res)
    elif x < 0:
        res = -1
        print(res)
    elif x == 0:
        res = 0
        print(res)


sign(x)