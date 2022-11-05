#!/usr/bin/python3

from .TreeNode import TreeNode

def maxPathSum(root):
    def maxPathSumRecursive(root):
        val, left, right = root.val, root.left, root.right
        if left == None and right == None:
            return (val, val)
        
        if left == None or right == None:
            child = left if right == None else right
            (childMaxPathSum, childPathSum) = maxPathSumRecursive(child)
            return (max(childMaxPathSum, val, val + childPathSum), val + (0 if childPathSum < 0 else childPathSum))
        
        (leftMaxPathSum, leftPathSum) = maxPathSumRecursive(root.left)
        (rightMaxPathSum, rightPathSum) = maxPathSumRecursive(root.right)
        return (\
            max(leftMaxPathSum, rightMaxPathSum, val, leftPathSum + val, rightPathSum + val, leftPathSum + rightPathSum + val),\
            max(val, val + leftPathSum, val + rightPathSum)\
            )
    
    (rev, ignored) = maxPathSumRecursive(root)
    return rev
    
        
