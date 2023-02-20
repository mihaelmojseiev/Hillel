def sum_symbol_codes(first, last):  # returns int
    sum = 0
    for i in range(ord(first), ord(last) + 1):
        sum += i
    return sum


def main():
    first = input(str("Введи первый символ:"))
    last = input(str("Введи первый символ:"))
    print(sum_symbol_codes(first, last))


if __name__ == "__main__":
    main()
