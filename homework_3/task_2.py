#a)
num = input("Введите целое(много можешь не вводить, запишет первые три): ")[:3]
a = int(num[0])
b = int(num[1])
c = int(num[2])
print(a+b+c)
#b)
num = input("Введите целое(много можешь не вводить, запишет первые три): ")[:3]
che=int(num)
def sum(no):
    return 0 if no == 0 else int(no % 10) + sum(int(no / 10))
print(sum(che))