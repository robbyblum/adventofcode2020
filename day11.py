# day 11: cellular automata, whee
import numpy as np
import pprint


# custom pretty-print wrapper for convenience)
def pprint_c(array):
    pprint.pprint(["".join(seq) for seq in array])


def check_neighbors(inarray, loc):
    # loc is a tuple (row_i, col_j)

    # define limits in each direction
    Nlim = -1
    Wlim = -1
    Slim, Elim = inarray.shape

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
        if nbr[0] < Slim and nbr[0] > Nlim:
            if nbr[1] < Elim and nbr[1] > Wlim:
                # check each neighbor now
                if inarray[nbr] == "#":
                    adjFilled += 1
    return adjFilled


def check_visible(inarray, inloc):
    # loc is a tuple (row_i, col_j)
    def step_loc(inloc, dirstr):
        # subfunction to step in a direction based on a string, why not
        # string can be composed of the characters NESW. I won't pass it
        # nonsensical stuff like NS or NESW or whatever, so I won't write it
        # to check the input logic very carefully
        i, j = inloc
        if "N" in dirstr:
            ii = i - 1
        elif "S" in dirstr:
            ii = i + 1
        else:
            ii = i

        if "W" in dirstr:
            jj = j - 1
        elif "E" in dirstr:
            jj = j + 1
        else:
            jj = j

        return (ii, jj)

    # define limits in each direction
    Nlim = -1
    Wlim = -1
    Slim, Elim = inarray.shape

    visibleFilled = 0
    for dirstr in ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]:
        loc = step_loc(inloc, dirstr)
        while (loc[0] < Slim and loc[0] > Nlim) and (loc[1] < Elim and loc[1] > Wlim):
            if inarray[loc] == "#":
                visibleFilled += 1
                break
            elif inarray[loc] == "L":
                break
            loc = step_loc(loc, dirstr)

    return visibleFilled


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

    # part 2: annoying sightline stuff instead of simple adjacency. Repeat the
    # same basic loop as before though.

    # make two arrays, one for step M, and one for step M+1 (N)
    arrayM = inarray.copy()
    arrayN = inarray.copy()
    iterationNum = 0
    while True:
        for loc, spot in np.ndenumerate(arrayM):
            if spot == "L":
                if check_visible(arrayM, loc) == 0:
                    arrayN[loc] = "#"
            elif spot == "#":
                if check_visible(arrayM, loc) >= 5:
                    arrayN[loc] = "L"

        # pprint_c(arrayN[:, :])
        # print()
        iterationNum += 1
        if (arrayM == arrayN).all():
            break
        else:
            arrayM = arrayN.copy()
    print(f"Part 2: {np.count_nonzero(arrayN == '#')}")


if __name__ == '__main__':
    main()
