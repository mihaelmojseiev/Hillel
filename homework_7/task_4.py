# Завдання 4.
#
# Написати функцію, що розраховує суму Unicode кодів усіх символів,
# що знаходяться між двома заданими символами включно. Наприклад,
# в функцію передаються символи 'a' та 'd', отже треба порахувати суму кодів символів 'a', 'b', 'c' та 'd', а це 97+98+99+100=394.
#
import string
def sum_symbol_codes(first, last): # returns int

def main():
    first = input(str('Введи первый символ:'))
    last = input(str('Введи первый символ:'))
    print(sum_symbol_codes(first, last))
if __name__ == '__main__':
    main()