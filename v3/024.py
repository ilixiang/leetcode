#!/usr/bin/python3

from ListNode import ListNode

def swapPairs(head):
    if head == None:
        return None

    k = 2
    prev = dummy = ListNode(0, head)

    i = 1
    last = head
    cur = head.next
    while cur != None:
        last.next = cur.next
        cur.next = prev.next
        prev.next = cur
        cur = last.next
        i += 1
        if i == k:
            i = 1
            prev = last
            last = cur
            cur = cur.next if cur != None else None
    
    if i != k:
        last = prev.next
        cur = last.next if last != None else None
        while cur != None:
            last.next = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = last.next

    return dummy.next
