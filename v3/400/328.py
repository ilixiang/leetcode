#!/usr/bin/python3

from ListNode import ListNode

def oddEventList(head):
    oddTail = odd = ListNode()
    evenTail = even = ListNode()
    cur = head
    while cur:
        oddTail.next = cur
        oddTail = cur
        if cur.next:
            cur = cur.next
            evenTail.next = cur
            evenTail = cur
        cur = cur.next
    oddTail.next = even.next
    evenTail.next = None
    return odd.next
