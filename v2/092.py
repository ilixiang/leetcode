#!/usr/bin/python3

from .ListNode import ListNode

def reverseBetween(head, left, right):
    dummy = ListNode(0, head)

    prev = dummy
    for i in range(0, left - 1):
        prev = prev.next
    first = prev.next
    for i in range(0, right - left):
        node = first.next
        first.next = node.next
        node.next = prev.next
        prev.next = node
    
    return dummy.next
