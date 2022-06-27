#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    inorderMap = {}
    for i in range(0, len(inorder)):
        inorderMap[inorder[i]] = i
    return buildTreeRecursive(postorder, len(postorder) - 1, inorder, 0, len(inorder), inorderMap)
    
def buildTreeRecursive(postorder, postorderIndex, inorder, inorderStart, inorderEnd, inorderMap):
    if inorderEnd == inorderStart:
        return None
    
    inorderIndex = inorderMap[postorder[postorderIndex]]
    rightTree = buildTreeRecursive(postorder, postorderIndex - 1, inorder, inorderIndex + 1, inorderEnd, inorderMap)
    leftTree = buildTreeRecursive(postorder, postorderIndex - inorderEnd + inorderIndex, inorder, inorderStart, inorderIndex, inorderMap)
    return TreeNode(inorder[inorderIndex], leftTree, rightTree)
    
print(buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))

