#!/usr/bin/python3

from ListNode import ListNode

def deleteDuplicates(head):
    if head == None:
        return None

    dummy = ListNode(0, head)
    prev, cur = dummy, head
    val, count = head.val, 0
    while cur != None:
        if cur.val == val:
            count += 1
            cur = cur.next
            continue

        if count > 1:
            prev.next = cur
        else:
            prev = prev.next
        val = cur.val
        cur = cur.next
        count = 1

    if count > 1:
        prev.next = cur
    else:
        prev = prev.next
    return dummy.next
