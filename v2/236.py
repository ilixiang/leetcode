#!/usr/bin/python3

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def lastCommonAncestor(root, v1, v2):
    if root == None:
        return None
    
    leftRev = lastCommonAncestor(root.left, v1, v2)
    rightRev = lastCommonAncestor(root.right, v1, v2)

    curRev = root.val if (root.val == v1 or root.val == v2) else None

    if leftRev == None and rightRev == None:
        return None if curRev == None else root.val
    
    if leftRev == None or rightRev == None:
        childRev = leftRev if rightRev == None else rightRev
        return curRev if curRev != None else childRev
    
    return root.val

if __name__ == '__main__':
    print(lastCommonAncestor(TreeNode(1, TreeNode(4, TreeNode(2), TreeNode(3))), 2, 3))
    print(lastCommonAncestor(TreeNode(1, TreeNode(2), TreeNode(3)), 1, 3))
    print(lastCommonAncestor(TreeNode(1, TreeNode(2), TreeNode(3)), 1, 2))

