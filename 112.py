#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if root == None:
        return False

    if root.left == None and root.right == None and targetSum == root.val:
        return True

    diff = targetSum - root.val
    return hasPathSum(root.left, diff) or hasPathSum(root.right, diff)

print(hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))), 22))

