#!/usr/bin/python3

class NumArray:
    def __init__(self, nums):
        prefixSums = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            prefixSums[i] = s
        self.prefixSums = prefixSums
    
    def sumRange(self, left, right):
        if left > right:
            return 0
        if left == 0:
            return self.prefixSums[right]
        return self.prefixSums[right] - self.prefixSums[left - 1]
