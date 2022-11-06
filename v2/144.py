#!/usr/bin/python3

def preorderTraversal(root):
    if root == None:
        return []
    
    rev = []
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        rev.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return rev
