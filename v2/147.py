#!/usr/bin/python3

from .ListNode import ListNode

def insertionSortList(head):
    if head == None:
        return None
    dummy = ListNode(0, head)
    prev = head
    while prev.next != None:
        node = prev.next
        insertionPrev = dummy
        while insertionPrev.next.val < node.val:
            insertionPrev = insertionPrev.next
        if insertionPrev == prev:
            prev = prev.next
        else:
            prev.next = node.next
            node.next = insertionPrev.next
            insertionPrev.next = node
    return dummy.next
