#!/usr/bin/python3

from .TreeNode import TreeNode

def isValidBST(root):
    return isValidBSTRecursive(root, None, None)

def isValidBSTRecursive(root, upper, down):
    if root == None:
        return True
    
    if upper != None and root.val >= upper:
        return False
    if down != None and root.val <= down:
        return False
    
    return isValidBSTRecursive(root.left, root.val, down) and isValidBSTRecursive(root.right, upper, root.val)

