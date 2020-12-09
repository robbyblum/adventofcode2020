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
            print(f"Part 1: {currentN}")
            break


if __name__ == '__main__':
    main()
