#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    if root == None:
        return True
    return isMirror(root.left, root.right)
    
def isMirror(left, right):
    if left == None and right == None:
        return True
    if left == None or right == None:
        return False

    return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

print(isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))
print(isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))))
