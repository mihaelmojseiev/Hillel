def index(lst, elem):  # returns integer or None
    for i in range(0, len(lst)):
        if lst[i] == elem:
            return i


def main():
    lst = ["M", "O", "I", "S", "E", "I", "E", "V"]
    print("Есть список ", lst)
    elem = input("Введи элемент списка(или нет): ")
    print(index(lst, elem))


if __name__ == "__main__":
    main()
