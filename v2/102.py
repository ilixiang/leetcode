#!/usr/bin/python3

from .TreeNode import TreeNode

def levelOrder(root):
    if root == None:
        return []
    
    rev = []
    queue = [root]
    while len(queue) != 0:
        size = len(queue)
        tmp = [0] * size
        for i in range(0, size):
            node = queue.pop(0)
            tmp[i] = node.val
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        rev.append(tmp)
    return rev
