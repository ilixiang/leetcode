#!/usr/bin/python3

from TreeNode import TreeNode

def pathSum(root, targetSum):
    if not root:
        return None
    tmp, rev = [], []
    def dfs(root, target):
        left, right = root.left, root.right

        diff = target - root.val
        tmp.append(root.val)
        if not left and not right:
            if diff == 0:
                rev.append(list(tmp))
        else:
            if left:
                dfs(left, diff)
            if right:
                dfs(right, diff)
        tmp.pop()
    dfs(root, targetSum)
    return rev
        