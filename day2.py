# day 2
import re

with open("input/day2.txt") as f:
    input = f.readlines()

numvalid = 0
for line in input:
    min, max, char, __, pw, __ = re.split("[-: \n]", line)
    if pw.count(char) >= int(min) and pw.count(char) <= int(max):
        numvalid += 1

print(numvalid)
