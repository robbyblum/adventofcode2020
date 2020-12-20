# day 15...puzzles

start = [9, 3, 1, 0, 8, 4]
start.reverse()
nums = start.copy()
print(start)
while len(nums) < 2020:
    n = nums[0]
    if nums.count(n) == 1:
        nums.insert(0, 0)
    else:
        nums.insert(0, nums.index(n, 1))
print("Part 1:", nums[0])
