#!/usr/bin/python3

from ListNode import ListNode

def partition(head, x):
    prev = delimiter = dummy = ListNode(0, head)
    while prev.next != None:
        cur = prev.next
        if cur.val < x:
            if delimiter == prev:
                delimiter = prev = cur
            else:
                prev.next = cur.next
                cur.next = delimiter.next
                delimiter.next = cur
                delimiter = cur
        else:
            prev = prev.next
    return dummy.next
