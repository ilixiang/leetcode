#!/usr/bin/python3

from ListNode import ListNode

def getIntersectionNode(headA, headB):
    n1, n2 = headA, headB
    while n1 and n2 and n1 != n2:
        n1 = n1.next
        n2 = n2.next
    
    if not n1 and not n2:
        return None
    if n1 == n2:
        return n1
    
    if not n1:
        n1 = headB
    else:
        n2 = headA
    while n1 and n2:
        n1 = n1.next
        n2 = n2.next
    
    if not n1:
        n1 = headB
    else:
        n2 = headA
    while n1 != n2:
        n1 = n1.next
        n2 = n2.next
    if not n1:
        return None
    return n1
