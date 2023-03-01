#!/usr/bin/python3

from ListNode import ListNode

def addTwoNumbers(l1, l2):
    n1, n2, carry = l1, l2, 0

    rev = ListNode()
    tail = rev
    while n1 != None and n2 != None:
        s = n1.val + n2.val + carry
        tail.next = ListNode(s % 10)
        carry = s // 10
        tail = tail.next
        n1, n2 = n1.next, n2.next
    
    n = n1 if n2 == None else n2
    while n != None:
        s = n.val + carry
        tail.next = ListNode(s % 10)
        carry = s // 10
        tail = tail.next
        n = n.next
    
    if carry != 0:
        tail.next = ListNode(carry)
    return rev.next
