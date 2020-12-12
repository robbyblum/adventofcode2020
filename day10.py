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


if __name__ == '__main__':
    main()
