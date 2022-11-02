#!/usr/bin/python3

from .ListNode import ListNode

def mergeTwoList(list1, list2):
    if list1 == None:
        return list2
    if list2 == None:
        return list1

    n1 = list1
    n2 = list2
    dummy = ListNode()
    n = dummy
    while n1 != None and n2 != None:
        if n1.val <= n2.val:
            n.next = n1
            n1 = n1.next
        else:
            n.next = n2
            n2 = n2.next
        n = n.next
    
    if n1 != None:
        n.next = n1
    if n2 != None:
        n.next = n2
    return dummy.next
