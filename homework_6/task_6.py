def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0


def main():
    x = int(input("Введи x: "))
    print(sign(x))


if __name__ == "__main__":
    main()
