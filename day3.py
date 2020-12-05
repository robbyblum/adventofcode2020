# day 3...

with open("input/day3.txt") as f:
    input = f.readlines()

# remove \n from lines, idk, maybe this'll help me in part 2?
for i, line in enumerate(input):
    input[i] = line.strip()

# starting position...this is overkill probably
x0, y0 = 0, 0

# dimensions of the array, I guess
xmax = len(input[0])  # 31
ymax = len(input)  # 323

# initialize at starting position
x, y, = x0, y0

n_trees = 0
# step through list and check for trees. move right modulo xmax, to handle
# of the periodicity thing
for y in range(1, ymax):
    x = (x + 3) % xmax
    if input[y][x] == "#":
        n_trees += 1

print(n_trees)
