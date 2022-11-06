#!/usr/bin/python3

class Node:
    def __init__(self, x, next = None, random = None):
        self.val = x
        self.next = next
        self.random = random

def copyRandomList(head):
    node = head
    while node != None:
        node.next = Node(node.val, node.next)
        node = node.next.next
    
    node = head
    while node != None:
        copyNode = node.next
        if node.random != None:
            copyNode.random = node.random.next
        node = copyNode.next

    node = head
    dummy = Node(0)
    prev = dummy
    while node != None:
        prev.next = node.next
        node.next = node.next.next
        prev = prev.next
        node = node.next

    return dummy.next
        
