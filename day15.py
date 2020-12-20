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
# print(nums)
print("Part 1:", nums[0])

# # this is a bad idea right...yeah this is a bad idea
# nums = start.copy()
# print(start)
# while len(nums) < 30000000:
#     n = nums[0]
#     if nums.count(n) == 1:
#         nums.insert(0, 0)
#     else:
#         nums.insert(0, nums.index(n, 1))
#     if len(nums) % 10000 == 0:
#         print(len(nums))
# print("Part 2:", nums[0])

# don't reverse it this time
start = [9, 3, 1, 0, 8, 4]
nums = {s: start.index(s) for s in start[0:-1]}
i = len(start) - 1
next = start[-1]
while i < 30000000:
    prev = next
    if prev in nums:
        next = i - nums[prev]
    else:
        next = 0
    nums[prev] = i
    i += 1
    # magical self-erasing "progress bar"
    if i % 100000 == 0:
        print('\x1b[1K', i, end='\r', flush=True)
print("\x1b[1KPart 2:", prev)
