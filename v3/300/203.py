#!/usr/bin/python3

from ListNode import ListNode

def removeElements(head, val):
    prev = dummy = ListNode(0, head)
    while prev.next:
        node = prev.next
        if node.val == val:
            prev.next = node.next
        else:
            prev = prev.next
    return dummy.next
