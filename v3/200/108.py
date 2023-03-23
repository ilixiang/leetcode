#!/usr/bin/python3

from TreeNode import TreeNode

def sortedArrayToBST(nums):
    def buildTree(l, r):
        if l > r:
            return None
        
        m = (l + r) >> 1
        return TreeNode(nums[m], buildTree(l, m - 1), buildTree(m + 1, r))
    return buildTree(0, len(nums) - 1)
