#!/usr/bin/python3

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        binaryIndexedTree = [0] * (1 + len(nums))
        for i in range(1, len(nums) + 1):
            tmp = 0
            for j in range(i - (i & (-i)) + 1, i + 1):
                tmp += nums[j - 1]
            binaryIndexedTree[i] = tmp
        self.binaryIndexedTree = binaryIndexedTree
        
    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index < len(self.nums) + 1:
            self.binaryIndexedTree[index] += diff
            index += index & (-index)

    def sumRange(self, left, right):
        leftSum = 0
        while left != 0:
            leftSum += self.binaryIndexedTree[left]
            left -= left & (-left)
        
        rightSum = 0
        right += 1
        while right != 0:
            rightSum += self.binaryIndexedTree[right]
            right -= right & (-right)
        return rightSum - leftSum
