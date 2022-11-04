#!/usr/bin/python3

from .TreeNode import TreeNode

def recoverTree(root):
    node = root
    first = None
    last = None

    prev = None
    stack = []
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev != None and node.val < prev.val:
                first = prev if first == None else first
                last = node
            prev = node
            node = node.right
    first.val, last.val = last.val, first.val
