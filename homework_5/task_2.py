import math


def triangle_square_and_perimeter(a, b):
    c_side = math.sqrt(a**2 + b**2)
    s = a * b / 2
    p = a + b + c_side
    return s, p


a = float(input('Длина а катета: '))
b = float(input('Длина b катета: '))


print('Площадь треугольника: ', triangle_square_and_perimeter(a,b)[0],
      '\nПериметр треугольника: ', triangle_square_and_perimeter(a,b)[1])
