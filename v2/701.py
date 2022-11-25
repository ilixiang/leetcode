#!/usr/bin/python3

from .TreeNode import TreeNode

def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    
    parent = root
    while parent != None:
        if val > parent.val:
            if parent.right != None:
                parent = parent.right
            else:
                parent.right = TreeNode(val)
                return root
        else:
            if parent.left != None:
                parent = parent.left
            else:
                parent.left = TreeNode(val)
                return root
    return root
