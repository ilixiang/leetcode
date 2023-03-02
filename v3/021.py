#!/usr/bin/python3

from ListNode import ListNode

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    cur = dummy

    n1, n2 = list1, list2
    while n1 != None and n2 != None:
        if n1.val < n2.val:
            cur.next = n1
            cur = n1
            n1 = n1.next
        else:
            cur.next = n2
            cur = n2
            n2 = n2.next
    
    n = n1 if n2 == None else n2
    cur.next = n

    return dummy.next
