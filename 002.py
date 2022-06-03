#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    n1 = l1
    n2 = l2
    result = ListNode()
    tail = result
    carry = 0
    while not (n1 == None and n2 == None):
        v1 = 0 if n1 == None else n1.val
        v2 = 0 if n2 == None else n2.val
        val = v1 + v2 + carry
        carry = val // 10
        tail.next = ListNode(val % 10)
        tail = tail.next
    tail.next = None if carry == 0 else ListNode(carry)
    return result.next

