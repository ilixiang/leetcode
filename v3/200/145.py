#!/usr/bin/python3

from TreeNode import TreeNode

def postorderTraversal(root):
    if not root:
        return []

    rev = []
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        rev.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    rev.reverse()
    return rev
