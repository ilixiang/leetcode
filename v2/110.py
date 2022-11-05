#!/usr/bin/python3

def isBalanced(root):
    def isBalancedRecursive(root):
        if root == None:
            return (True, 0)
        (leftBalanced, leftHeight) = isBalancedRecursive(root.left)
        if not leftBalanced:
            return (False, None)
        (rightBalanced, rightHeight) = isBalancedRecursive(root.right)
        if not rightBalanced:
            return (False, None)
        return (abs(leftHeight - rightHeight) <= 1, 1 + max(leftHeight, rightHeight))
    
    (balanced, height) = isBalancedRecursive(root)
    return balanced
