#!/usr/bin/python3

from TreeNode import TreeNode

def kthSmallest(root, k):
    stack = []
    cur, node = 1, root
    while node or len(stack) != 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if cur == k:
                return node.val
            cur += 1
            node = node.right
    return None
