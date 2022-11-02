#!/usr/bin/python3

def minDepth(root):
    if root == None:
        return 0
    queue = [root]
    otherQueue = []
    depth = 1
    while len(queue) != 0:
        node = queue.pop(0)
        if node.left == None and node.right == None:
            return depth

        if node.left != None:
            otherQueue.append(node.left)
        if node.right != None:
            otherQueue.append(node.right)

        if len(queue) == 0:
            depth = depth + 1
            tmp = queue
            queue = otherQueue
            otherQueue = tmp
    return depth

