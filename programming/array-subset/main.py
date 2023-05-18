import sys


def get_all_subset(nums):
    subset = [[]]
    for num in nums:
        subset += [i + [num] for i in subset]
    return subset

def get_all_subset_with_dfs_recursive(nums):
    subset = []
    def dfs(nums, index, path):
        subset.append(path)
        for i in range(index, len(nums)):
            dfs(nums, i + 1, path + [nums[i]])
    dfs(nums, 0, [])
    return subset

for line in sys.stdin:
    nums = [int(i) for i in line.split(',')]
    subset = get_all_subset_with_dfs_recursive(nums)

    print(subset)
