# Завдання 1.
#
# Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
# Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів.
import math
def degrees2radians(degrees):
    radians = (degrees * math.pi)/180
    return radians

degrees = (int(input('Введи градусы: ')))

print(degrees2radians(degrees))