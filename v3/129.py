#!/usr/bin/python3

from TreeNode import TreeNode

def sumNumbers(root):
    if root == None:
        return 0
    
    def dfs(root, parentSumNumber):
        right, left, val = root.left, root.right, root.val
        rootSumNumber = parentSumNumber * 10 + val
        if not left and not right:
            return rootSumNumber
        
        if not left or not right:
            child = left if not right else right
            return dfs(child, rootSumNumber)
        
        return dfs(left, rootSumNumber) + dfs(right, rootSumNumber)
    return dfs(root, 0)
