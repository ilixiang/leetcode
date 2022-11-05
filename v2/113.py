#!/usr/bin/python3

from .TreeNode import TreeNode

def pathSum(root, targetSum):
    tmp = []
    rev = []
    def pathSumRecursive(root, target):
        if root == None:
            return
        
        diff = target - root.val
        left, right = root.left, root.right

        tmp.append(root.val)
        if left == None and right == None:
            if root.val == target:
                rev.append(list(tmp))
            tmp.pop()
            return
        
        pathSumRecursive(root.left, diff)
        pathSumRecursive(root.right, diff)
        tmp.pop()

    pathSumRecursive(root, targetSum)
    return rev
