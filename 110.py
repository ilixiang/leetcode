#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left =left
        self.right = right

def isBalanced(root):
    (balanced, height) = isBalancedRecursive(root)
    return balanced

def isBalancedRecursive(root):
    if root == None:
        return (True, 0)

    (leftBalanced, leftHeight) = isBalancedRecursive(root.left)
    (rightBalanced, rightHeight) = isBalancedRecursive(root.right)
    balanced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
    height = max(leftHeight, rightHeight) + 1
    return (balanced, height)

print(isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

