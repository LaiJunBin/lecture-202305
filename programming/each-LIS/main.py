import sys
from bisect import bisect_right



def binary_search_right(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] <= target:
            left = middle + 1
        else:
            right = middle - 1

    return left

for line in sys.stdin:
    nums = [int(i) for i in line.split(',')]

    current_sequence = []
    result = []

    for num in nums:
        index = bisect_right(current_sequence, num)

        if index == len(current_sequence):
            current_sequence.append(num)
        else:
            current_sequence[index] = num

        result.append(index + 1)
    
    print(result)
    

