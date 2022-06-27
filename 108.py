#!/usr/bin/python3

def sortedArrayToBST(nums):
    return sortedArrayToBSTRecursive(nums, 0, len(nums))

def sortedArrayToBSTRecursive(nums, low, high):
    if low >= high:
        return None
    mid = (low + high) // 2
    leftTree = sortedArrayToBSTRecursive(nums, low, mid)
    rightTree = sortedArrayToBSTRecursive(nums, mid + 1, high)
    return TreeNode(nums[mid], leftTree, rightTree)

