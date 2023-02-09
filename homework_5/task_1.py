# Завдання 1.
#
# Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
# Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів.
# import math
# def degrees2radians(degrees):
#     radians = (degrees * math.pi)/180
#     return radians
from bs4 import BeautifulSoup
import requests
def currensy():
    url = 'https://ru.onlinemschool.com/math/formula/sine_table/'
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html.parser')
    table = soup.find("table", {"class": "oms_mnt"})
    print(soup.prettify())
currensy()





    # table = soup.find("table", {"class": "sc-1x32wa2-1 dYkgjk"})
    # tr = table.find("p", {"class": "sc-1x32wa2-9 glerpA"})
    # tr = tr.text[:5]
    # tr = tr.replace(",", ".")
    # tr = float(tr)
    # return (tr)

# degrees = (int(input('Введи градусы: ')))
#
# print(degrees2radians(degrees))