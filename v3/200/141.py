#!/usr/bin/python3

from ListNode import ListNode

def hasCycle(head):
    if not head:
        return False
    
    slow, fast = head, head.next
    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    return slow == fast
    