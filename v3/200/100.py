#!/usr/bin/python3

from TreeNode import TreeNode

def isSameTree(p, q):
    if p == None and q == None:
        return True
    
    if p == None or q == None:
        return False
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
