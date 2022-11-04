#!/usr/bin/python3

from .ListNode import ListNode

def partition(head, x):
    if head == None:
        return None
    
    dummy = ListNode(0, head)
    delimiter = dummy
    prev = dummy
    while prev.next != None:
        if prev.next.val < x:
            node = prev.next
            if prev != delimiter:
                prev.next = node.next
                node.next = delimiter.next
                delimiter.next = node
            else:
                prev = node
            delimiter = node
            continue
        prev = prev.next
    return dummy.next
