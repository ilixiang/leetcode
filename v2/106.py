#!/usr/bin/python3

from .TreeNode import TreeNode

def buildTree(inorder, postorder):
    inorderMap = {}
    for i in range(0, len(inorder)):
        inorderMap[inorder[i]] = i

    def buildTreeRecursive(i1, i2, p1, p2):
        if i1 == i2:
            return None
        
        i = inorderMap[postorder[p2 - 1]]
        left = buildTreeRecursive(i1, i, p1, p1 + i - i1)
        right = buildTreeRecursive(i + 1, i2, p1 + i - i1, p2 - 1)
        return TreeNode(postorder[p2 - 1], left, right)
    return buildTreeRecursive(0, len(inorder), 0, len(postorder))
