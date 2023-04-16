#!/usr/bin/python3

from TreeNode import TreeNode

def invertTree(root):
    if not root:
        return None
    left, right = root.left, root.right
    root.left = invertTree(right)
    root.right = invertTree(left)
    return root
