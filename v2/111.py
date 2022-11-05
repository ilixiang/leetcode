#!/usr/bin/python3

def minDepth(root):
    if root == None:
        return 0

    def minDepthRecursive(root):
        left, right = root.left, root.right
        if left == None and right == None:
            return 1

        if left == None:
            return 1 + minDepthRecursive(right)
        if right == None:
            return 1 + minDepthRecursive(left)
        return 1 + min(minDepthRecursive(left), minDepthRecursive(right))
    return minDepthRecursive(root)
