#!/usr/bin/python3

class Node:
    def __init__(self, val = 0, left = None, right = None, n = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = n

def connect(root):
    if not root:
        return None
    
    queue = [root]
    while len(queue) != 0:
        c = len(queue)
        prev = None
        while c != 0:
            n = queue.pop(0)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
            if prev != None:
                prev.next = n
            prev = n
        prev.next = None
        c -= 1
    return root
