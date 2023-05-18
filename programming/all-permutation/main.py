import sys


def get_all_permutation(nums, current=[], result=[]):
    if len(nums) == 0:
        result += [current]
        return result
    
    for i in range(len(nums)):
        result = get_all_permutation(nums[:i] + nums[i + 1:], current + [nums[i]], result)

    return result

def get_all_permutation_with_simple_solution(nums):
    import itertools
    return list(itertools.permutations(nums))

for line in sys.stdin:
    nums = [int(i) for i in line.split(',')]
    result = get_all_permutation(nums)

    print(result)
