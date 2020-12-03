# day 2
import re

with open("input/day2.txt") as f:
    input = f.readlines()

# part 1
numvalid = 0
for line in input:
    min, max, char, __, pw, __ = re.split("[-: \n]", line)
    if pw.count(char) >= int(min) and pw.count(char) <= int(max):
        numvalid += 1

print(numvalid)


# part 2
numvalid = 0
for line in input:
    ind1, ind2, char, __, pw, __ = re.split("[-: \n]", line)
    ind1 = int(ind1) - 1
    ind2 = int(ind2) - 1
    check1 = pw[ind1] == char
    check2 = pw[ind2] == char
    if (check1 and not check2) or (not check1 and check2):
        numvalid += 1

print(numvalid)
