#!/usr/bin/python3

class Node:
    def __init__(self, val, left, right, n):
        self.val = val
        self.left = left
        self.right = right
        self.next = n
    
def connect(root):
    if root == None:
        return
    
    dummy = Node()
    queue = [root]
    while len(queue) != 0:
        size = len(queue)
        prev = dummy
        while size != 0:
            node = queue.pop(0)
            prev.next = node
            prev = node
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            size -= 1
        prev.next = None
    dummy.next = None
    return root
