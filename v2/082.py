#!/usr/bin/python3

from .ListNode import ListNode

def deleteDuplicates(head):
    if head == None:
        return None

    dummy = ListNode(0, head)
    delimiter = dummy
    n = head
    while n != None:
        if n.next != None and n.val == n.next.val:
            val = n.val
            while n != None and n.val != val:
                n = n.next
            continue
        delimiter.next = n
        delimiter = n
        n = n.next
    delimiter.next = None
    return dummy.next
