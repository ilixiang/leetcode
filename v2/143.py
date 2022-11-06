#!/usr/bin/python3

from .ListNode import ListNode

def recordList(head):
    if head == None or head.next == None:
        return
    
    slow = head
    fast = head.next.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    l1 = head
    l2 = slow.next
    slow.next = None

    dummy = ListNode(0, l2)
    while l2.next != None:
        node = l2.next
        l2.next = node.next
        node.next = dummy.next
        dummy.next = node
    l2 = dummy.next

    prev = dummy
    count = 0
    while l1 != None and l2 != None:
        if count & 1 == 0:
            prev.next = l1
            prev = l1
            l1 = l1.next
        else:
            prev.next = l2
            prev = l2
            l2 = l2.next
        count += 1
    if l1 != None:
        prev.next = l1
    if l2 != None:
        prev.next = l2
    
    return dummy.next

