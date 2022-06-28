#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    result = []
    path = []
    pathSumRecursive(root, targetSum, path, result)
    return result

def pathSumRecursive(root, targetSum, path, result):
    if root == None:
        return

    if root.left == None and root.right == None and targetSum == root.val:
        path.append(targetSum)
        result.append(list(path))
        path.pop()
        return

    path.append(root.val)
    diff = targetSum - root.val
    pathSumRecursive(root.left, diff, path, result)
    pathSumRecursive(root.right, diff, path, result)
    path.pop()


print(pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))), 22))

