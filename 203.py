#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def removeElements(head, val):
    if head == None:
        return None
    dummy = ListNode(0, head)
    previous = dummy
    current = head
    while current != None:
        if current.val == val:
            previous.next = current.next
        else:
            previous = current
        current = previous.next
    return dummy.next

