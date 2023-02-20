import random


def main():
    number = random.randint(1, 10)
    print("Число загадано")

    while True:
        guess_number = int(input("Введи число: "))

        if guess_number > number:
            print("Число больше, давай еще")

        if guess_number < number:
            print("Число меньше, давай еще")

        if guess_number == number:
            print("Угадал")
            break


if __name__ == "__main__":
    main()
