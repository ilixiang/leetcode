#!/usr/bin/python3

from TreeNode import TreeNode

def levelOrder(root):
    if root == None:
        return []

    queue = [root]
    rev = []
    while len(queue) != 0:
        c = len(queue)
        tmp = [0] * c
        for i in range(c):
            n = queue.pop(0)
            tmp[i] = n.val
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        rev.append(tmp)
    return rev

