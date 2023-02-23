def calculate_wheat_chess_position(kilograms):
    seeds_kg_input = float(input("Введи кол-во кг зерна: "))
    seeds_count_from_input = int(seeds_kg_input / kilograms * 1000000)
    square = 1
    seeds_on_square = 1
    seeds_count_on_board = 0
    while seeds_count_on_board < seeds_count_from_input:
        seeds_count_on_board += seeds_on_square
        if seeds_count_on_board >= seeds_count_from_input:
            break
        seeds_on_square *= 2
        square += 1
    column = (square - 1) // 8 + 1
    row = chr((square - 1) % 8 + ord("A"))
    return column, row


def main():
    kilograms = 0.03584
    print(calculate_wheat_chess_position(kilograms))


if __name__ == "__main__":
    main()
