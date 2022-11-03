#!/usr/bin/python3

from .ListNode import ListNode

def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy
    prev = dummy
    reversedCount = 0
    while prev.next != None:
        if prev == groupPrev:
            prev = prev.next
            reversedCount += 1
            continue
        node = prev.next
        prev.next = node.next
        node.next = groupPrev.next
        groupPrev.next = node
        reversedCount += 1
        if reversedCount == k:
            reversedCount = 0
            groupPrev = prev

    if reversedCount != 0:
        prev = groupPrev
        while prev.next != None:
            if prev != groupPrev:
                node = prev.next
                prev.next = node.next
                node.next = groupPrev.next
                groupPrev.next = node
            else:
                prev = prev.next
    return dummy.next