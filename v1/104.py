#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root == None:
        return 0
    queue = [root]
    otherQueue = []
    depth = 0
    while len(queue) != 0:
        node = queue.pop(0)
        if node.left != None:
            otherQueue.append(node.left)
        if node.right != None:
            otherQueue.append(node.right)

        if len(queue) == 0:
            tmp = queue
            queue = otherQueue
            otherQueue = tmp
            depth = depth + 1
    return depth

print(maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

