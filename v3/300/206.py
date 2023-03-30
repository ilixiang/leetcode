#!/usr/bin/python3

from ListNode import ListNode

def reverseList(head):
    if not head:
        return None
    dummy = ListNode(0, head)
    prev = head
    while prev.next:
        node = prev.next
        prev.next = node.next
        node.next = dummy.next
        dummy.next = node
    return dummy.next
