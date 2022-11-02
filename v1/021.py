#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n
def mergeTwoLists(list1, list2):
    h = ListNode()
    t = h
    n1 = list1
    n2 = list2
    while n1 != None and n2 != None:
        if n1.val < n2.val:
            t.next = n1
            t = n1
            n1 = n1.next
        else:
            t.next = n2
            t = n2
            n2 = n2.next
    t.next = n2 if n1 == None else n1
    return h.next