#!/usr/bin/python3

from .TreeNode import TreeNode

def hasPathSum(root, targetSum):
    if root == None:
        return False

    left, right = root.left, root.right
    if left == None and right == None and targetSum == root.val:
        return True
    
    return hasPathSum(left, targetSum - root.val) or hasPathSum(right, targetSum - root.val)
