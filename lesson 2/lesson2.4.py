#Завдання 4.
#Написати програму, що за допомогою функції input() запитує кількість гривень і потім виводить еквіваленте число доларів США (курс довільний -- можна підгледіти на будь-яку дату у вашому банку або у НБУ). Наприклад:
#>>> Введіть кількість гривень:
#... 74.63
#>>> Станом на 25 серпня 2022 року це становить 2.0 Долари США :(
from decimal import *
from datetime import datetime
current_datetime = datetime.now()
a = Decimal(input("Введіть кількість гривень: "))
b = a / Decimal('39.5')
print("Станом на ",current_datetime," це становить" ,b, " Долари США")