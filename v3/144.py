#!/usr/bin/python3

from TreeNode import TreeNode

def preorderTraversal(root):
    if not root:
        return []

    rev = []
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        rev.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return rev
