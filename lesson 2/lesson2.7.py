#Завдання 7. ** (не обов'язкове, не оцінюється)
#Напишіть програму, що запитує у користувача довільне ціле число, а виводить його двійкове представлення.
#Для розрахунку використати функцію divmod(). Не можна використовувати фукнцію bin() -- треба послідовно ділити число
#та додавати 0 або 1 до результату (Підказка: '1'+'0'+'1' == '101'). Цикли та умовні конструкції не використовувати.
#Прийняти, що введене число не більше, ніж 63. Результат завжди буде займати 6 символів, нулі попереду значення прийнятні для значень, що менше, ніж 32.

a = int(input("Целое число: "))
if a < 63:
    print('Нормально, оно меньше 63')
elif a == 63:
    print('Нормально, это 63')
else:
    print('Давай по новой, много')
xo,yo = divmod(a,2)
xu,yu = divmod(xo,2)
xy,yy = divmod(xu,2)
xt,yt = divmod(xy,2)
xr,yr = divmod(xt,2)
xe,ye = divmod(xr,2)
s = ' '.join([str(ye),str(yr),str(yt),str(yy),str(yu),str(yo)])
print(s)