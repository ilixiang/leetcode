#!/usr/bin/python3

from TreeNode import TreeNode

def countNodes(root):
    def treeHeight(root):
        rev = 0
        while root:
            rev += 1
            root = root.left
        return rev
    
    def recursive(root):
        if not root:
            return 0

        leftHeight = treeHeight(root.left)
        rightHeight = treeHeight(root.right)
        if leftHeight > rightHeight:
            return 2 ** rightHeight + recursive(root.left)
        else:
            return 2 ** leftHeight + recursive(root.right)
    return recursive(root)
