#!/usr/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binaryTreePaths(root):
    if root is None:
        return []
    pathVals = []
    result = []
    treePath(root, pathVals, result)
    return result

def treePath(node, pathVals, result):
    pathVals.append(node.val)
    if node.left == None and node.right == None:
        result.append('->'.join(pathVals))
        pathVals.pop()
        return

    if node.left != None:
        treePath(node.left, pathVals, result)

    if node.right != None:
        treePath(node.right, pathVals, result)
    pathVals.pop()

