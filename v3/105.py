#!/usr/bin/python3

from TreeNode import TreeNode

def buildTree(preorder, inorder):
    inorderMap = {}
    for i in range(len(inorder)):
        inorderMap[inorder[i]] = i

    def buildTreeRecursive(i1, j1, i2, j2):
        if i1 > j1:
            return None

        d = inorderMap[preorder[i1]]
        return TreeNode(inorder[d], buildTreeRecursive(i1 + 1, d + i1 - i2, i2, d - 1), buildTreeRecursive(d + i1 - i2 + 1, j1, d + 1, j2))
    return buildTreeRecursive(0, len(preorder) - 1, 0, len(inorder) - 1)
