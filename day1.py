import numpy as np

input = np.loadtxt("input/day1.txt", dtype="int")

L = len(input)

sumarray = np.zeros((L, L))
for m, num1 in enumerate(input):
    for n, num2 in enumerate(input):
        sumarray[m, n] = num1 + num2

sum2020 = np.unique(np.nonzero(sumarray == 2020))
print(sum2020)
print(input[sum2020].prod())

sumarray = np.zeros((L, L, L))
for i, num1 in enumerate(input):
    for j, num2 in enumerate(input):
        for k, num3 in enumerate(input):
            sumarray[i, j, k] = num1 + num2 + num3

sum2020 = np.unique(np.nonzero(sumarray == 2020))
print(sum2020)
print(input[sum2020].prod())
