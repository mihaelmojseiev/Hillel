def main():
    lst1 = [5, "9", 0, "452", 6.5, "6", 1, 2]
    lst2 = [472, 326, 1, 999.0, "1101000", "99", 9, "20", 863, "0"]
    sorted_lst1 = sorted(lst1, key=lambda x: float(x))
    sorted_lst2 = sorted(lst2, key=lambda x: str(x)[0])
    print(sorted_lst1)
    print(sorted_lst2)


if __name__ == "__main__":
    main()
