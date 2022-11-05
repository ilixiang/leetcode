#!/usr/bin/python3

from .TreeNode import TreeNode

def buildTree(preorder, inorder):
    def buildTreeRecursive(preorder, p1, p2, inorder, i1, i2):
        if i1 == i2:
            return None
        i = i1
        while i < i2 and preorder[p1] != inorder[i]:
            i += 1
        left = buildTreeRecursive(preorder, p1 + 1, p1 + 1 + i - i1, inorder, i1, i)
        right = buildTreeRecursive(preorder, p1 + 1 + i - i1, p2, inorder, i + 1, i2)
        return TreeNode(preorder[p1], left, right)
    
    return buildTreeRecursive(preorder, 0, len(preorder), inorder, 0, len(inorder))
