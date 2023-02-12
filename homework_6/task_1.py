def is_even(number):
    try:
        number = int(number)
        if number % 2 == 0:
            print(bool(True))
        if number % 2 == 1:
            print(bool(False))
    except:
        print('этот символ не номер')


is_even(input('введи число: '))