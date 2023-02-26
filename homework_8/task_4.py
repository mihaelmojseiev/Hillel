def gen_primes():  # returns list of ints
    primes = []
    for num in range(2, 101):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes


def main():
    print(gen_primes())


if __name__ == "__main__":
    main()
