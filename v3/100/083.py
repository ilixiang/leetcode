#!/usr/bin/python3

from ListNode import ListNode

def deleteDuplicates(head):
    if head == None:
        return None

    prev, cur = head, head.next
    while cur != None:
        if cur.val == prev.val:
            cur = cur.next
            continue
        prev.next = cur
        prev = cur
        cur = cur.next
    prev.next = None
    return head
