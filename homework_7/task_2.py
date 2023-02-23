def main():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
        elif fizzbuzz % 5 == 0:
            print("Buzz")
        elif fizzbuzz % 3 == 0:
            print("Fizz")
        else:
            print(fizzbuzz)


if __name__ == "__main__":
    main()
