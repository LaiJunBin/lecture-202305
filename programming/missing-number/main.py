import sys


for line in sys.stdin:
    nums = [int(i) for i in line.strip().split(',')]
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i + 1:
            print(i + 1)
            break
