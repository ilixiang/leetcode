#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if root == None:
        return []
    result = []
    currentQueue = [root]
    otherQueue = []
    while len(currentQueue) != 0:
        node = currentQueue.pop(0)
        if node.left != None:
            otherQueue.append(node.left)
        if node.right != None:
            otherQueue.append(node.right)

        if len(currentQueue) == 0:
            result.append(node.val)
            tmp = currentQueue
            currentQueue = otherQueue
            otherQueue = tmp
    return result

print(rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
print(rightSideView(TreeNode(1, None, TreeNode(3))))
