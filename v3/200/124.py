#!/usr/bin/python3

from TreeNode import TreeNode

def maxPathSum(root):
    if root == None:
        return 0
    
    def recursive(root):
        left, right, val = root.left, root.right, root.val
        if not left and not right:
            return (val, val)
        
        if not left or not right:
            child = left if right == None else right
            (childMaxPathSum, childMaxHalfPathSum) = recursive(child)
            maxHalfPathSum = val if childMaxHalfPathSum < 0 else (val + childMaxHalfPathSum)
            return (max(childMaxPathSum, maxHalfPathSum), maxHalfPathSum)
        
        (leftMaxPathSum, leftMaxHalfPathSum) = recursive(left)
        (rightMaxPathSum, rightMaxHalfPathSum) = recursive(right)

        return (max(leftMaxPathSum, rightMaxPathSum, val, val + leftMaxHalfPathSum, val + rightMaxHalfPathSum, val + leftMaxHalfPathSum + rightMaxHalfPathSum), max(val, val + leftMaxHalfPathSum, val + rightMaxHalfPathSum))
    return recursive(root)[0]
        