def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

numb = (int(input('Введи номер: ')))

if numb <= 0:
   print("Ввёл отрицательное")
else:
   print("Последовательность такая:")
   for i in range(numb):
       print(fibonacci(i))
