import pickle


def copydeep(obj):
    return pickle.loads(pickle.dumps(obj))


def main():
    lst1 = ["a", 1, 2.0, ["b"]]
    lst2 = copydeep(lst1)
    print(lst1)
    print(lst2)


if __name__ == "__main__":
    main()
