import numpy as np

input = np.loadtxt("input/day1.txt", dtype="int")

L = len(input)

sumarray = np.zeros((L, L))
for m in np.arange(L):
    for n in np.arange(L):
        sumarray[m, n] = input[m] + input[n]

sum2020 = np.unique(np.nonzero(sumarray == 2020))
print(sum2020)
print(input[sum2020].prod())

sumarray = np.zeros((L, L, L))
for i in np.arange(L):
    for j in np.arange(L):
        for k in np.arange(L):
            sumarray[i, j, k] = input[i] + input[j] + input[k]

sum2020 = np.unique(np.nonzero(sumarray == 2020))
print(sum2020)
print(input[sum2020].prod())
