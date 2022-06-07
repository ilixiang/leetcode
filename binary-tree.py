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

def isCompleteBinaryTree(root):
    if root == None:
        return True
    queue = [root]
    onlyLeaf = False
    while len(queue) != 0:
        node = queue.pop(0)
        if node.left == None and node.right != None:
            return False
        if onlyLeaf and (node.left != None or node.right != None):
            return False
        if node.left == None or node.right == None:
            onlyLeaf = True

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return True

def isBalancedBinaryTree(root):
    if root is None:
        return (True, 0)
    left = root.left
    right = root.left
    
    isLeftBalanced, leftHeight = isBalancedTree(left)
    isRightBalanced, rightHeight = isBalancedTree(right)

    return isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) <= 1
