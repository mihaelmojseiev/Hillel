#Завдання 2a.
#З допомогою Python порахувати наступні вирази для a=1, b=5, c=4 (використати функцію sqrt з модулю math):

import math
a=1
b=5
c=4
x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print(x1)
print(x2)

#Завдання 2b.
#Порахувати ту ж формулу, але для значень a=2, b=5, c=2 (для обчислення кореню використати оператор **)

import math
a=2
b=5
c=2
x3=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x4=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print(x3)
print(x4)
