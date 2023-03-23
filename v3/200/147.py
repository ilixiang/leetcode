#!/usr/bin/python3

from ListNode import ListNode

def insertSortList(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0, head)
    prev = head
    while prev.next:
        node = prev.next
        insertPrev = dummy
        while insertPrev != prev and insertPrev.next.val < node.val:
            insertPrev = insertPrev.next

        if insertPrev != prev:
            prev.next = node.next
            node.next = insertPrev.next
            insertPrev.next = node
        else:
            prev = prev.next
    return dummy.next