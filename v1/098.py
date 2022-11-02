#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

def isValidBST(root):
    return isValidBSTRecursive(root, None, None)

def isValidBSTRecursive(root, lower, upper):
    if root == None:
        return True

    val = root.val
    return (lower == None or (lower != None and lower < val)) \
        and (upper == None or (upper != None and val < upper)) \
        and isValidBSTRecursive(root.left, lower, val) \
        and isValidBSTRecursive(root.right, val, upper)

root = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(isValidBST(root))

