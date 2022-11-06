#!/usr/bin/python3

def detectCycle(head):
    if head == None or head.next == None:
        return None
    
    fast = head.next.next
    slow = head.next
    while fast != None and fast.next != None and slow != fast:
        fast = fast.next.next
        slow = slow.next

    if slow != fast:
        return None
    
    pos = 0
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        pos += 1
    return pos
