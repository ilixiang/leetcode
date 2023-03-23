#!/usr/bin/python3

from TreeNode import TreeNode

def inorderTraversal(root):
    node = root
    stack = []
    rev = []
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            rev.append(node.val)
            node = node.right
    return rev
