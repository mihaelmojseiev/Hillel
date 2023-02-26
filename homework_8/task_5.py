import random


def get_max_digit(number):
    max_digit = 0
    while number > 0:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        number //= 10
    return max_digit


def main():
    number = random.randint(10**11, (10**12) - 1)
    print(number)
    print(get_max_digit(number))


if __name__ == "__main__":
    main()
