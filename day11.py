# day 11: cellular automata, whee
import numpy as np
import pprint


# custom pretty-print wrapper for convenience)
def pprint_c(array):
    pprint.pprint(["".join(seq) for seq in array])


def check_neighbors(inarray, loc):
    # loc is a tuple (row_i, col_j)
    # construct neighbors
    north = (loc[0], loc[1] + 1)
    east = (loc[0] + 1, loc[1])
    south = (loc[0], loc[1] - 1)
    west = (loc[0] - 1, loc[1])
    ne = (loc[0] + 1, loc[1] + 1)
    se = (loc[0] + 1, loc[1] - 1)
    sw = (loc[0] - 1, loc[1] - 1)
    nw = (loc[0] - 1, loc[1] + 1)

    adjFilled = 0
    for nbr in (north, east, south, west, ne, se, sw, nw):
        if nbr[0] < inarray.shape[0] and nbr[0] > -1:
            if nbr[1] < inarray.shape[1] and nbr[1] > -1:
                # check each neighbor now
                if inarray[nbr] == "#":
                    adjFilled += 1
    return adjFilled


def main():
    inraw = np.loadtxt("input/day11.txt", dtype="unicode_")
    inarray = np.array([[a for a in inraw[i]] for i in range(len(inraw))])
    Nrows, Ncols = inarray.shape
    # print(M, N)
    # pprint_c(inarray)
    # test = check_neighbors(inarray, (0, 0))
    # print(test)

    # make two arrays, one for step M, and one for step M+1 (N)
    arrayM = inarray.copy()
    arrayN = inarray.copy()
    iterationNum = 0
    while True:
        for loc, spot in np.ndenumerate(arrayM):
            if spot == "L":
                if check_neighbors(arrayM, loc) == 0:
                    arrayN[loc] = "#"
            elif spot == "#":
                if check_neighbors(arrayM, loc) >= 4:
                    arrayN[loc] = "L"

        iterationNum += 1
        if (arrayM == arrayN).all():
            break
        else:
            arrayM = arrayN.copy()
    # pprint_c(arrayN)
    # print(iterationNum)
    print(f"Part 1: {np.count_nonzero(arrayN == '#')}")


if __name__ == '__main__':
    main()
