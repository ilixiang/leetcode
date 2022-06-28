#!/usr/bin/python3

class Node:
    def __init__(self, val = 0, left = None, right = None, n = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = n

def connect(root):
    if root == None:
        return root

    queue = [root]
    dummy = Node()
    current = dummy
    while len(queue) != 0:
        length = len(queue)
        count = 0
        while count < length:
            node = queue.pop(0)
            current.next = node
            current = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            count = count + 1
        current = dummy
    return root

