import sys


def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1

for line in sys.stdin:
    data = line.strip().split()
    nums = [int(num) for num in data[0][1:-1].split(',')]
    target = int(data[-1])
    index = binarySearch(nums, target)
    print(index)
