#!/usr/bin/python3

from .ListNode import ListNode

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    node = dummy
    for i in range(0, n):
        node = node.next

    prev = dummy
    while node.next != None:
        prev = prev.next
        node = node.next
    
    prev.next = prev.next.next
    return dummy.next
