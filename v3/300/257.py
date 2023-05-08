#!/usr/bin/python3

from TreeNode import TreeNode

def binaryTreePaths(root):
    if not root:
        return []
    
    tmp, rev = [], []
    def dfs(root):
        tmp.append(str(root.val))
        left, right = root.left, root.right
        if not left and not right:
            rev.append('->'.join(tmp))
        
        if left:
            dfs(left)
        if right:
            dfs(right)
        tmp.pop()
    dfs(root)
    return rev
