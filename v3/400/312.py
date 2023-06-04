#!/usr/bin/python3

def maxCoins(nums):
    nums = [1] + nums + [1]
    m = len(nums)
    cache = [[-1 for j in range(m)] for i in range(m)]
    def dp(left, right):
        if left > right:
            return 0
        rev = cache[left][right]
        if rev != -1:
            return rev
        rev = 0
        for mid in range(left, right + 1):
            tmp = nums[left - 1] * nums[mid] * nums[right + 1]
            rev = max(rev, tmp + dp(left, mid - 1) + dp(mid + 1, right))
        cache[left][right] = rev
        return rev
    return dp(1, m - 2)
