#!/usr/bin/python3

from .ListNode import ListNode

def hasCycle(head):
    if head == None or head.next == None:
        return False
    fast = head.next.next
    slow = head.next
    while fast != None and fast.next != None and slow != fast:
        fast = fast.next.next
        slow = slow.next
    return slow == fast

