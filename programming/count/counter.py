import sys
from collections import Counter


for line in sys.stdin:
    nums = line.strip()[1:-1].split(',')
    counts = Counter(nums)
    
    max_count = 0
    max_key = nums[0]
    for key in counts:
        if counts[key] >= max_count:
            max_count = counts[key]
            if ord(max_key) > ord(key):
                max_key = key

    print(max_key)
