#!/usr/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preOrder(root):
    if root is None:
        return
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        # process node
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)

def inOrder(root):
    if root is None:
        return
    stack = []
    node = root
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            # process node
            node = node.right

def postOrder(root):
    if root is None:
        return
    stack1 = [root]
    stack2 = []
    while len(stack1) != 0:
        node = stack1.pop()
        stack2.append(node)
        if node.right != None:
            stack1.append(node.right)
        if node.left != None:
            stack1.append(node.left)

    while len(stack2) != 0:
        node = stack2.pop()
        # process node
