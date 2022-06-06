#!/usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCircle(head):
    if head.next == None:
        return False

    fastNode = head.next.next
    slowNode = head.next
    while fastNode != slowNode and fastNode != None:
        if fastNode.next == None:
            return False
        fastNode = fastNode.next.next
        slowNode = slowNode.next

    return fastNode != None

