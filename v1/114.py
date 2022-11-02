#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if root == None:
        return
    dummy = TreeNode()
    current = dummy
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
        node.left = None
        current.right = node
        current = current.right

