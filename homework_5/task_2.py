import math

def triangle_square_and_perimeter(a_side, b_side):
    c_side = math.sqrt(a_side**2 + b_side**2)
    s = (a_side * b_side) / 2
    p = a_side + b_side + c_side
    return(s,p)

a_side = float(input('Длина а катета: '))
b_side = float(input('Длина b катета: '))

print('Площадь треугольника: ', triangle_square_and_perimeter(a_side,b_side)[0], '\nПериметр треугольника: ', triangle_square_and_perimeter(a_side,b_side)[1])
