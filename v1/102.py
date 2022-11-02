#!/usr/bin/python3

def levelOrder(root):
    if root == None:
        return []

    queue = [root]
    otherQueue = []
    levelVals = []
    result = []
    while len(queue) != None:
        node = queue.pop(0)
        tmp.append(node.val)
        if node.left != None:
            otherQueue.append(node.left)
        if node.right != None:
            otherQueue.append(node.right)

        if len(queue) == 0:
            result.append(levelVals)
            levelVals = []
            tmp = queue
            queue = otherQueue
            otherQueue = tmp
    return result

