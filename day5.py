# day 5


def seat_id(row, column):
    return row * 8 + column


def convert_row(rowstr):
    return int(rowstr.replace("F", "0").replace("B", "1"), 2)


def convert_col(colstr):
    return int(colstr.replace("L", "0").replace("R", "1"), 2)


def main():
    import numpy as np

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
    print("Part 1:", max(seats_id))

    # Part 2: this can be done in fewer lines but who cares
    seats_id.sort()
    dseats = np.diff(np.array(seats_id))
    i_seat_before = np.nonzero(dseats - 1)[0][0]
    seat_before = seats_id[i_seat_before]
    my_seat = seat_before + 1
    print("Part 2:", my_seat)


if __name__ == '__main__':
    main()
