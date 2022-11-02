#!/usr/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if root == None or root == p or root == q:
        return root

    leftCommonAncestor = lowestCommonAncestor(root.left, p, q)
    rightCommonAncestor = lowestCommonAncestor(root.right, p, q)

    if (leftCommonAncestor != None and rightCommonAncestor != None):
        return root

    return leftCommonAncestor if rightCommonAncestor == None else rightCommonAncestor


