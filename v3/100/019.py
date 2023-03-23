#!/usr/bin/python3

from ListNode import ListNode

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    r = head
    for i in range(n):
        r = r.next
    l = dummy
    while r != None:
        l = l.next
        r = r.next

    l.next = l.next.next
    return dummy.next
    
