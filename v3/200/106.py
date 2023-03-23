#!/usr/bin/python3

from TreeNode import TreeNode

def buildTree(inorder, postorder):
    m = len(inorder)
    inorderMap = {}
    for i in range(m):
        inorderMap[inorder[i]] = i
    
    def buildTreeRecursive(i1, j1, i2, j2):
        if i2 > j2:
            return None
        
        rootVal = postorder[j2]
        d = inorderMap[rootVal]
        return TreeNode(rootVal, buildTreeRecursive(i1, d - 1, i2, i2 - i1 + d - 1), buildTreeRecursive(d + 1, j1, j2 - j1 + d, j2 - 1))
    return buildTreeRecursive(0, m - 1, 0, m - 1)
