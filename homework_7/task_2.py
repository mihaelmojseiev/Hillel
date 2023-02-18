for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('FizzBuzz')
        continue
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        continue
    elif fizzbuzz % 3 == 0:
        print('Fizz')
        continue
    print(fizzbuzz)
