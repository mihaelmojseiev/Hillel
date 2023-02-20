def chessboard(x1, y1, x2, y2):
    rx = abs(x1 - x2)
    ry = abs(y1 - y2)
    if rx == 1 and ry == 2 or rx == 2 and ry == 1:
        return True
    else:
        return False


def main():
    x1 = ord(input("Введи стартовую букву столбца типа a-h: "))
    y1 = int(input("Введи стартовую цифру строки типа 1-8: "))
    x2 = ord(input("Введи конечную букву столбца типа a-h: "))
    y2 = int(input("Введи конечную цифру строки типа 1-8: "))
    print(chessboard(x1, y1, x2, y2))


if __name__ == "__main__":
    main()
