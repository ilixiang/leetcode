#!/usr/bin/python3

from .ListNode import ListNode

def addTwoNumber(l1, l2):
    dummy = ListNode()
    r = dummy

    n1 = l1
    n2 = l2
    carry = 0
    while n1 != None and n2 != None:
        s = n1.val + n2.val + carry
        r.next = ListNode(s % 10)
        carry = s // 10

        n1 = n1.next
        n2 = n2.next
        r = r.next
    
    while n1 != None:
        s = n1.val + carry
        r.next = ListNode(s % 10)
        carry = s // 10

        n1 = n1.next
        r = r.next
    
    while n2 != None:
        s = n2.val + carry
        r.next = ListNode(s % 10)
        carry = s // 10

        n2 = n2.next
        r = r.next
    
    if carry != 0:
        r.next = ListNode(carry)
    return dummy.next


