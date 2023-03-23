#!/usr/bin/python3

from TreeNode import TreeNode

def isValidBST(root):
    stack = []
    node = root
    prev = None
    while node != None or len(stack) != 0:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev != None and prev >= node.val:
                return False
            prev = node.val
            node = node.right
    return True
