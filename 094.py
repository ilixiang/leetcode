#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    vals = []
    s = []
    node = root
    while node != None or len(s) != 0:
        while node != None:
            s.append(node)
            node = node.left
        node = s.pop()
        vals.append(node.val)
        node = node.right
    return vals

print(inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))

