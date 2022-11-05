#!/usr/bin/python3

from .TreeNode import TreeNode

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None

    def sortedArrayToBSTRecursive(low, high):
        if low == high:
            return None
        mid = (low + high) // 2
        left = sortedArrayToBSTRecursive(low, mid)
        right = sortedArrayToBSTRecursive(mid + 1, high)
        return TreeNode(nums[mid], left, right)
    
    return sortedArrayToBSTRecursive(0, len(nums))
