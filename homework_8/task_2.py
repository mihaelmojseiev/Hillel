def copydeep(obj):
    if isinstance(obj, (str, int, float, bool)):
        return obj
    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            new_list.append(copydeep(item))
        return new_list
    elif isinstance(obj, tuple):
        new_tuple = []
        for item in obj:
            new_tuple.append(copydeep(item))
        return tuple(new_tuple)


def main():
    lst1 = ["a", 1, 2.0, ["b"]]
    lst2 = copydeep(lst1)
    print("Исходник ", lst1)
    print("Копия    ", lst2)


if __name__ == "__main__":
    main()
