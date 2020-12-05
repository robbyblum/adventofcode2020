# day 5


def seat_id(row, column):
    return row * 8 + column


def convert_row(rowstr):
    return int(rowstr.replace("F", "0").replace("B", "1"), 2)


def convert_col(colstr):
    return int(colstr.replace("L", "0").replace("R", "1"), 2)


def main():
    with open("input/day5.txt") as f:
        input = f.readlines()
        input = [i.strip() for i in input]

    row1 = convert_row(input[0][0:7])
    col1 = convert_col(input[0][7:10])
    print(row1, col1)

    seats_rc = []
    seats_id = []
    for line in input:
        row = convert_row(line[0:7])
        col = convert_col(line[7:10])
        seats_rc.append((row, col))
        seats_id.append(seat_id(row, col))

    # Part 1:
    print(max(seats_id))


if __name__ == '__main__':
    main()
