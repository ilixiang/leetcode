#!/usr/bin/python3

def levelOrderBottom(root):
    if root == None:
        return []
    queue = [root]
    rev = []
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
    rev.reverse()
    return rev
