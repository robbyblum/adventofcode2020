# day 10


def load_sort_adaptors(f):
    adaptors = [int(a) for a in f.readlines()]
    adaptors.sort()
    return adaptors


def main():
    with open("input/day10.txt") as f:
        adaptors = load_sort_adaptors(f)
    # print(adaptors)
    L = len(adaptors)
    device_J = max(adaptors) + 3
    Jdiff = [min(adaptors)]
    for i, a in enumerate(adaptors):
        if i < L - 1:
            Jdiff.append(adaptors[i + 1] - a)
        else:
            Jdiff.append(device_J - a)
    # print(Jdiff)
    n1 = Jdiff.count(1)
    n3 = Jdiff.count(3)
    print(f"Part 1: {n1} x {n3} = {n1 * n3}")

    # part 2: The 3-jolt gaps always have to be bridged in the same way, which
    # constrains the problem somewhat. Also, the longest run of consecutive
    # joltages I have is 4. counting permutations of such subsections by hand
    # gives me the following:
    # 4 in a row: 6
    # 3 in a row: 4
    # 2 in a row: 2
    # 1 in a row: 1, obviously
    # so if I count how many 1 1 1 1, 1 1 1, and 1 1 instances I have, then do
    # some sort of correct combinatorics with these subsets...which is where
    # I'm getting stuck. For now, let's program in my counting-of-ones stuff:
    i = 0
    n_ones = 0
    runs_ones = []
    while i < len(Jdiff):
        if Jdiff[i] == 1:
            n_ones += 1
        else:
            runs_ones.append(n_ones)
            n_ones = 0
        i += 1
    # print(runs_ones)
    print(runs_ones.count(0), runs_ones.count(1), runs_ones.count(2),
          runs_ones.count(3), runs_ones.count(4))
    print((2**6) * (4**10) * (6**8), "but this is too low.")
    # This gives me the same as my hand count did, so I don't know what I'm
    # doing wrong...oh I was miscounting combinations. For 4 in a row it's 7,
    # not 6.
    print("Part 2:", (2**6) * (4**10) * (7**8))


if __name__ == '__main__':
    main()
