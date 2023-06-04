#!/usr/bin/python3

def lengthOfLIS(nums):
    tailNums = [0] * len(nums)
    length = 0
    for num in nums:
        if length == 0 or tailNums[length - 1] < num:
            tailNums[length] = num
            length += 1
            continue

        target = -1
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) >> 1
            if tailNums[mid] >= num:
                target = mid
                right = mid - 1
            else:
                left = mid + 1
        tailNums[target] = num
    return length
