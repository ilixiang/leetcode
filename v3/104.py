#!/usr/bin/python3

from TreeNode import TreeNode

def maxDepth(root):
    if root == None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
