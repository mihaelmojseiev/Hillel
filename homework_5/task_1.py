import math


def degrees2radians(degrees):
    radians = (degrees * math.pi)/180
    return radians


degrees = int(input('Введи градусы: '))

print(degrees2radians(degrees), '\nЗначення косинуса для 60: ',
      math.cos(60), '\nЗначення косинуса для 45: ',
      math.cos(45), '\nЗначення косинуса для 40: ' ,
      math.cos(40))