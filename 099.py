#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    if root == None:
        return
    prev = None
    first = None
    second = None
    n = root
    s = []
    while len(s) != 0 or n != None:
        if n != None:
            s.append(n)
            n = n.left
        else:
            n = s.pop()
            if prev != None and prev.val > n.val:
                if first == None:
                    first = prev
                second = n
            prev = n
            n = n.right
    tmp = first.val
    first.val = second.val
    second.val = tmp

root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
recoverTree(root)

