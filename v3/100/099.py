#!/usr/bin/python3

from TreeNode import TreeNode

def recoverTree(root):
    left = right = None
    prev = None
    node = root
    stack = []
    while node != None or len(stack) != 0:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev != None and prev.val > node.val:
                if left == None:
                    left, right = prev, node
                else:
                    right = node
                    left.val, right.val = right.val, left.val
                    return
            prev = node
            node = node.right
    left.val, right.val = right.val, left.val
