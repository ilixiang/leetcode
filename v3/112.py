#!/usr/bin/python3

from TreeNode import TreeNode

def hasPathSum(root, targetSum):
    if not root:
        return False

    def dfs(root, target):
        left, right = root.left, root.right
        if not left and not right:
            return root.val == target
        
        diff = target - root.val
        return (left and dfs(left, diff)) or (right and dfs(right, diff))

    return dfs(root, targetSum)
