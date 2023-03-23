#!/usr/bin/python3

from ListNode import ListNode

def reverseBetween(head, left, right):
    prev = dummy = ListNode(0, head)

    i = 1
    while i < left:
        prev = prev.next
        i += 1
    
    tail = prev.next
    cur = tail.next
    while i < right:
        tail.next = cur.next
        cur.next = prev.next
        prev.next = cur
        cur = tail.next
        i += 1
    return dummy.next
