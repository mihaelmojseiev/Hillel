def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)


def main():
     numb = (int(input('Введи номер: ')))

     if numb <= 0:
         print("Ввёл отрицательное")
     else:
         print("Последовательность такая:")
         fibonaccci = fibonacci(numb - 1)
         print(fibonaccci)


if __name__ == '__main__':
   main()