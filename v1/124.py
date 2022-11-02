#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    return maxPathRecursive(root)[0]

def maxPathRecursive(root):
    val = root.val
    if root.left == None and root.right == None:
        return (val, val)
    elif root.left != None and root.right == None:
        left = maxPathRecursive(root.left) if root.left != None else None
        return (max(val + left[1], left[0], val), max(0, left[1]) + val)
    elif root.left == None and root.right != None:
        right = maxPathRecursive(root.right) if root.right != None else None
        return (max(val + right[1], right[0], val), max(0, right[1]) + val)
    else:
        left = maxPathRecursive(root.left) if root.left != None else None
        right = maxPathRecursive(root.right) if root.right != None else None
        return (max(val + left[1] + right[1], val + left[1], val + right[1], left[0], right[0], val), max(left[1], right[1], 0) + val)

print(maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
print(maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

