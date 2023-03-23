#!/usr/bin/python3

from TreeNode import TreeNode

def isSymmetrix(root):
    if root == None:
        return True
    
    def isMirror(p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)
    return isMirror(root.left, root.right)

