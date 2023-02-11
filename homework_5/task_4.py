def my_sum(*lst, start=0):
    summ = sum(lst, dop_start)
    return summ


list_data = input('Введи список чисел: ').split()
dop_start = int(input('Введи стартовое значение: '))

lst = []

for element in list_data:
    if element.isdigit():
        lst.append(int(element))
    else:
        print(f'{element} - не число ')
        print('Давай заново')
        exit()

print(f'{my_sum(*lst)} твоя сумма чисел')