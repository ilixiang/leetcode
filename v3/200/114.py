#!/usr/bin/python3

from TreeNode import TreeNode

def flatten(root):
    if not root:
        return None

    prev = dummy = TreeNode(0)
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        prev.left = None
        prev.right = node
        prev = node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return dummy.right

