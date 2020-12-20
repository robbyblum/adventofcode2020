# day 17: oh good, more Conway. Now in *three* dimensions. Fortunately we're
# only doing six cycles this time. My input is an 8x8 slice.
import numpy as np
import pprint


# let's just copy and paste in a bunch of stuff from day 11!
# custom pretty-print wrapper for convenience
def pprint_c(array):
    pprint.pprint(["".join(seq) for seq in array])
    # print("\n".join(["".join(seq) for seq in array]))


def check_neighbors(inarray, loc):
    # loc is a tuple (x, y, z)
    x, y, z = loc
    # define upper limits
    xd, yd, zd = inarray.shape

    # i really should have done day 11 like this instead
    # construct a slicer!
    s = np.s_[max(0, x - 1):min(xd, x + 2),
              max(0, y - 1):min(yd, y + 2),
              max(0, z - 1):min(zd, z + 2)]

    return np.count_nonzero(inarray[s] == '#') - (inarray[x, y, z] == '#')


def main():
    inraw = np.loadtxt("input/day17.txt", dtype="unicode_", comments=None)
    inarray = np.array([[a for a in inraw[i]] for i in range(len(inraw))])
    inA, inB = inarray.shape
    inC = 1
    # pprint_c(inarray)

    Nsteps = 6
    A, B, C = np.array([inA, inB, inC]) + Nsteps * 2
    # # make two arrays, one for step M, and one for step M+1 (N)
    arrayM = np.full((A, B, C), '.', dtype="unicode_")
    arrayM[Nsteps:Nsteps + inA, Nsteps:Nsteps + inB, Nsteps] = inarray
    arrayN = arrayM.copy()
    # pprint_c(arrayM[:, :, Nsteps])
    iterationNum = 0
    for i in range(6):
        for loc, spot in np.ndenumerate(arrayM):
            numadj = check_neighbors(arrayM, loc)
            if spot == ".":
                if numadj == 3:
                    arrayN[loc] = "#"
            else:  # spot == "#"
                if numadj < 2 or numadj > 3:
                    arrayN[loc] = "."

        arrayM = arrayN.copy()
    print(f"Part 1: {np.count_nonzero(arrayN == '#')}")


if __name__ == '__main__':
    main()
