#!/usr/bin/python3

def minSubArrayLenSolutionOne(target, nums):
    numSums = [0] * (len(nums) + 1)
    rev = len(nums) + 1
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        diff = s - target
        if diff >= 0:
            left, right = 0, i
            start = 0
            while left <= right:
                mid = (left + right) >> 1
                if numSums[mid] <= diff:
                    start = mid
                    left = mid + 1
                else:
                    right = mid - 1
            rev = min(rev, i + 1 - start)
        numSums[i + 1] = s
    return 0 if rev == len(nums) + 1 else rev

def minSubArrayLenSolutionTwo(target, nums):
    s = 0
    left = 0
    rev = len(nums) + 1
    for right in range(len(nums)):
        s += nums[right]
        if s < target:
            continue
        while left < right and (s - nums[left]) >= target:
            s -= nums[left]
            left += 1
        rev = min(rev, right - left + 1)
    return 0 if rev == (len(nums) + 1) else rev
