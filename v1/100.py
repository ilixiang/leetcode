#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if (p == None and q != None) or (p != None and q == None):
        return False

    if p == None and q == None:
        return True

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
print(isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))))
