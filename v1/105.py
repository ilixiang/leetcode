#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    inorderMap = {}
    for i in range(0, len(inorder)):
        inorderMap[inorder[i]] = i
    return buildTreeRecursive(preorder, 0, inorder, 0, len(inorder), inorderMap)
    
def buildTreeRecursive(preorder, preorderIndex, inorder, inorderStart, inorderEnd, inorderMap):
    if inorderEnd == inorderStart:
        return None
    
    inorderIndex = inorderMap[preorder[preorderIndex]]
    leftTree = buildTreeRecursive(preorder, preorderIndex + 1, inorder, inorderStart, inorderIndex, inorderMap)
    rightTree = buildTreeRecursive(preorder, preorderIndex + inorderIndex - inorderStart + 1, inorder, inorderIndex + 1, inorderEnd, inorderMap)
    return TreeNode(inorder[inorderIndex], leftTree, rightTree)
    
print(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))

