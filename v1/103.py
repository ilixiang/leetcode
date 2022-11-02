#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right =right

def zigzagLevelOrder(root):
    if root == None:
        return []

    stack = [root]
    otherStack = []
    reverse = False
    levelVals = []
    result = []
    while len(stack) != 0:
        node = stack.pop()
        levelVals.append(node.val)
        if reverse:
            if node.right != None:
                otherStack.append(node.right)
            if node.left != None:
                otherStack.append(node.left)
        else:
            if node.left != None:
                otherStack.append(node.left)
            if node.right != None:
                otherStack.append(node.right)

        if len(stack) == 0:
            result.append(levelVals)
            levelVals = []
            reverse = not reverse
            tmp = stack
            stack = otherStack
            otherStack = tmp
    return result

print(zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

