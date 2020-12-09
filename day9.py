# day 9
import numpy as np


def main():
    input = np.loadtxt("input/day9.txt", dtype=int)
    L = len(input)

    for N in range(25, L):
        currentN = input[N]
        prev25 = input[N - 25:N]
        for i, prevN in enumerate(prev25):
            for prevM in prev25[i + 1:]:
                testsum = prevN + prevM
                if testsum == currentN:
                    break
            else:
                # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break
        else:
            print(f"Part 1: {currentN} at index {N}")
            break

    part1answer = currentN
    part1index = N
    # part 2: let's suppose that the contiguous region is always *before* the
    # special number. This is reasonable because while the sequence doesn't
    # increase monotonically, it does increase overall. If this doesn't work
    # I'll reevaluate.

    for n in range(part1index - 1):
        foundit = False
        listsum = [input[n]]
        for m in range(n + 1, part1index):
            listsum.append(input[m])
            if sum(listsum) < part1answer:
                continue
            elif sum(listsum) > part1answer:
                break
            elif sum(listsum) == part1answer:
                foundit = True
                print("you got it")
                break
        if foundit:
            break
    # print(n, m)
    # print(listsum)
    # print(min(listsum), max(listsum))
    print(f"Part 2: {min(listsum) + max(listsum)}")

if __name__ == '__main__':
    main()
