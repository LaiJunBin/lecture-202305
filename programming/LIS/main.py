import sys


def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

def longest_increasing_subsequence_effiently(nums):
    dp = []
    for num in nums:
        i = 0
        j = len(dp)
        while i != j:
            mid = (i + j) // 2
            if dp[mid] < num:
                i = mid + 1
            else:
                j = mid
        
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
        
    return len(dp)

def longest_increasing_subsequence_with_bisect(nums):
    from bisect import bisect_left
    dp = []
    for num in nums:
        i = bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)
   

for line in sys.stdin:
    nums = [int(num) for num in line.strip().split(',')]
    output = longest_increasing_subsequence_effiently(nums)
    print(output)

    