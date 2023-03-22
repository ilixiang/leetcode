#!/usr/bin/python3

from ListNode import ListNode

def reorderList(head):
    slow = fast = ListNode(0, head)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    tail = slow.next
    if not tail:
        return
        
    cur = tail.next
    while cur:
        tail.next = cur.next
        cur.next = slow.next
        slow.next = cur
        cur = tail.next
    
    cur = head
    while slow.next and cur != slow:
        node = slow.next
        slow.next = node.next
        node.next = cur.next
        cur.next = node
        cur = node.next
