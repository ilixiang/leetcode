#!/usr/bin/python3

def invertTree(root):
    if root == None:
        return None
    left = root.right
    right = root.left

    root.left = invertTree(left)
    root.right = invertTree(right)

    return root

