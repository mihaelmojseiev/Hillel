import math

def degrees2radians(degrees):
    radians = (degrees * math.pi)/180
    return radians

degrees = int(input('Введи градусы: '))

print(degrees2radians(degrees), '\nЗначення косинуса для 60: ', math.cos(60), '\nЗначення косинуса для 45: ', math.cos(45), '\nЗначення косинуса для 40: ', math.cos(40))


# попытался вывести через гугл калькулятор - пишет None, не смог еще разобраться
# import requests
# from bs4 import BeautifulSoup
# grad = int(input('Введи градусы: '))
#
# def cosin():
#     url = 'http://surl.li/euocd'
#     source = requests.get(url)
#     soup = BeautifulSoup(source.content, 'html.parser')
#     # input = soup.find("input", {"data-ved": "2ahUKEwilhuG96Ir9AhWQFcAKHR3KCpcQ5Wp6BAgHEAM"})
#     input_tag = soup.find("input", {"data-ved": "2ahUKEwilhuG96Ir9AhWQFcAKHR3KCpcQ5Wp6BAgHEAM"})
#     input_tag['value'] = int(grad)
#     answer = soup.find("input", {"data-ved": "2ahUKEwilhuG96Ir9AhWQFcAKHR3KCpcQ52p6BAgHEAU"})
#     return (answer)
#     # answer = soup.find_all("span", {"class": "oms_1"})
#     # soup.div.span.insert_after(int(grad), insert)
#     # print(f'{answer}')
#     #
# print(cosin())
