# day 6...
# count distinct questions or whatever


# parse forms from input file. Split by group!
def parse_forms(file):
    raw = file.read()
    # Ths smushes each group's responses together, to better facilitate part 1.
    # I'm sure I'll regret this in part 2.
    grouplist = ["".join(p.splitlines()) for p in raw.split("\n\n")]
    # pdict = [dict(field.split(":") for field in p) for p in plist]
    return grouplist


def main():
    with open("input/day6.txt") as f:
        grouplist = parse_forms(f)

    # part 1
    sumcounts = 0
    for group in grouplist:
        sumcounts += len({c for c in group})
    print("Part 1:", sumcounts)


if __name__ == '__main__':
    main()
