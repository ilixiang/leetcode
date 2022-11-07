#!/usr/bin/python3

from .TreeNode import TreeNode

def rightSideView(root):
    if root == None:
        return []

    rev = []
    queue = [root]
    while len(queue) != 0:
        size = len(queue)
        rev.append(queue[0].val)
        while size != 0:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            size -= 1
    return rev
