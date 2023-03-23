#!/usr/bin/python3

from TreeNode import TreeNode

def levelOrderBottom(root):
    if root == None:
        return []

    rev = []
    queue = [root]
    while len(queue) != 0:
        m = len(queue)
        tmp = [0] * m
        for i in range(m):
            node = queue.pop(0)
            tmp[i] = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        rev.append(tmp)
    rev.reverse()
    return rev
