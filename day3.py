# day 3...


# OK for part 2 I need to have this in a function
def check_trees(map, slopex, slopey):

    # starting position, hardcoded for now
    x0, y0 = 0, 0
    # initialize at starting position
    x, y, = x0, y0

    # dimensions of the array
    xmax = len(map[0])
    ymax = len(map)

    n_trees = 0
    # step through list and check for trees. move right modulo xmax, to handle
    # of the periodicity thing
    for y in range(slopey, ymax, slopey):
        x = (x + slopex) % xmax
        if map[y][x] == "#":
            n_trees += 1

    return n_trees


def main():
    from math import prod

    with open("input/day3.txt") as f:
        input = f.readlines()

    # remove \n from lines, so that len(input[i]) gives the actual width
    for i, line in enumerate(input):
        input[i] = line.strip()

    # part 1
    n_trees = check_trees(input, 3, 1)
    print("Part 1:", n_trees)

    # part 2:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []

    for slope in slopes:
        trees.append(check_trees(input, *slope))

    print("Part 2:", prod(trees), trees)


if __name__ == '__main__':
    main()
