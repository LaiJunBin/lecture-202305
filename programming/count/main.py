import sys


for line in sys.stdin:
    nums = line.strip()[1:-1].split(',')
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = 0
    max_key = nums[0]
    for key in counts:
        if counts[key] >= max_count:
            max_count = counts[key]
            if ord(max_key) > ord(key):
                max_key = key

    print(max_key)
