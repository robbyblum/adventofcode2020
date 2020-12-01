import numpy as np
import time

input = np.loadtxt("input/day1.txt", dtype="int")

start = time.time()
for num1 in input:
    for num2 in input:
        if num1 + num2 == 2020:
            print(f"{num1} + {num2} == 2020")
            print(f"{num1} * {num2} == {num1 * num2}")
            break
    else:
        # Continue if the inner loop wasn't broken.
        continue
    # Inner loop was broken, break the outer.
    break
part1 = time.time()

for num1 in input:
    for num2 in input:
        for num3 in input:
            if num1 + num2 + num3 == 2020:
                print(f"{num1} + {num2} + {num3} == 2020")
                print(f"{num1} * {num2} * {num3} == {num1 * num2 * num3}")
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
    else:
        # Continue if the inner loop wasn't broken.
        continue
    # Inner loop was broken, break the outer.
    # is there a better way to do this? Idk, probably
    break
part2 = time.time()

# just for fun, timing it
print(f"part 1: {part1 - start} sec")
print(f"part 2: {part2 - part1} sec")
