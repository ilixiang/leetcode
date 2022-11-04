#!/usr/bin/python3

from .ListNode import ListNode

def rotateRight(head, k):
    if head == None:
        return head

    length = 0
    n = head
    while n.next != None:
        length += 1
        n = n.next
    tail = n
    length += 1

    k = k % length
    if k == 0:
        return head

    i = 1
    n = head
    while i != length - k:
        n = n.next
        i += 1
    
    tail.next = head
    head = n.next
    n.next = None
    return head
