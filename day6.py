# day 6...
# count distinct questions or whatever


# parse forms from input file. Split by group!
def parse_forms(file):
    raw = file.read()
    # Ths smushes each group's responses together, to better facilitate part 1.
    # I'm sure I'll regret this in part 2.
    # grouplist = ["".join(p.splitlines()) for p in raw.split("\n\n")]

    # yeah that doesn't work for part 2 but I can make it work. here
    grouplist = [p.splitlines() for p in raw.split("\n\n")]
    return grouplist


def main():
    with open("input/day6.txt") as f:
        group_list = parse_forms(f)

    # part 1
    sumcounts1 = 0
    sumcounts2 = 0
    for group in group_list:
        groupset = {c for c in ''.join(group)}
        sumcounts1 += len(groupset)
        sumcounts2 += sum([all([d in e for e in group]) for d in groupset])
    print("Part 1:", sumcounts1)
    print("Part 2:", sumcounts2)


if __name__ == '__main__':
    main()
