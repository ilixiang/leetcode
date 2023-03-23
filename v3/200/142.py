#!/usr/bin/python3

from ListNode import ListNode

def detectCycle(head):
    if not head or not head.next:
        return None
    slow, fast = head.next, head.next.next
    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    
    if slow != fast:
        return None
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
