import math


def cone_square_and_volume(radius, height):
    square = math.pi * radius**2 + math.pi * radius * math.sqrt(radius**2 + height**29)
    volume = 1 / 3 * math.pi * radius**2 * height
    return square, volume


radius = float(input('Введи радиус: '))
height = float(input('Введи радиус высоту: '))

print('Площадь конуса: ', cone_square_and_volume(radius, height)[0],
      '\nОбъем конуса: ', cone_square_and_volume(radius , height)[1])
