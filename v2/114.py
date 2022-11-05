#!/usr/bin/python3

from .TreeNode import TreeNode

def flatten(root):
    if root == None:
        return []

    stack = [root]
    prev = TreeNode()
    while len(stack) != 0:
        node = stack.pop()
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
            node.left = None

        prev.right = node
        prev = node
    