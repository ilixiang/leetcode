#!/usr/bin/python3

class Node:
    def __init__(self, x, n = None, random = None):
        self.val = x
        self.next = n
        self.random = random

def copyRandomList(head):
    if not head:
        return None

    node = head
    while node:
        nodeCopy = Node(node.val, node.next)
        node.next = nodeCopy
        node = nodeCopy.next

    node = head
    while node:
        nodeCopy = node.next
        nodeCopy.random = node.random.next if node.random else None
        node = nodeCopy.next
    
    node = head
    dummy = tail = Node(0)
    while node:
        nodeCopy = node.next
        tail.next = nodeCopy
        tail = nodeCopy
        node.next = nodeCopy.next
        node = nodeCopy.next
    return dummy.next
