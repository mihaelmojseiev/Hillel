def fibonacci(val):
    fib1 = 0
    fib2 = 1

    for n in range(val-2):
        vrem = fib1 + fib2
        fib1 = fib2
        fib2 = vrem

    return fib2


def main():
    val = int(input("Введи число: "))
    print(fibonacci(val))


if __name__ == '__main__':
    main()