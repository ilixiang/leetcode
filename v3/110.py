#!/usr/bin/python3

from TreeNode import TreeNode

def isBalanced(root):
    def recursive(root):
        if root == None:
            return (0, True)
        
        leftRev = recursive(root.left)
        rightRev = recursive(root.right)
        return (1 + max(leftRev[0], rightRev[0]), leftRev[1] and rightRev[1] and abs(leftRev[0] - rightRev[0]) <= 1)
    return recursive(root)[1]
