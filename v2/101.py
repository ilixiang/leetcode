#!/usr/bin/python3

from .TreeNode import TreeNode

def isSymmetric(root):
    if root == None:
        return True

    def isSymmetricRecursive(left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        
        return left.val == right.val\
            and isSymmetricRecursive(left.left, right.right)\
            and isSymmetricRecursive(left.right, right.left)

    return isSymmetricRecursive(root.left, root.right)

