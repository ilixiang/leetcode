#!/usr/bin/python3

from TreeNode import TreeNode

def minDepth(root):
    if root == None:
        return 0
    rev = 1
    queue = [root]
    while len(queue) != 0:
        c = len(queue)
        while c > 0:
            n = queue.pop(0)
            if not n.left and not n.right:
                return rev
            else:
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            c -= 1
        rev += 1
    return rev
