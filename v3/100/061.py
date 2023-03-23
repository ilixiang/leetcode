#!/usr/bin/python3

from ListNode import ListNode

def rotateRight(head, k):
    if head == None:
        return None

    n = dummy = ListNode(0, head)

    length = 0
    while n.next != None:
        length += 1
        n = n.next
    tail = n
    
    k %= length
    n = dummy
    for i in range(0, length - k):
        n = n.next
    tail.next = dummy.next
    dummy.next = n.next
    n.next = None
    
    return dummy.next
