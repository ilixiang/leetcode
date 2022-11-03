#!/usr/bin/python3

from .ListNode import ListNode

def mergeKLists(lists):
    if len(lists) == 0:
        return None

    return mergeKListsRecursive(lists, 0, len(lists))

def mergeKListsRecursive(lists, left, right):
    if left >= right:
        return None
    
    if left + 1 == right:
        return lists[left]
    
    mid = (left + right) // 2
    l1 = mergeKListsRecursive(lists, left, mid)
    l2 = mergeKListsRecursive(lists, mid, right)

    n1 = l1
    n2 = l2
    dummy = ListNode()
    n = dummy
    while n1 != None and n2 != None:
        if n1.val <= n2.val:
            n.next = n1
            n = n1
            n1 = n1.next
        else:
            n.next = n2
            n = n2
            n2 = n2.next
    
    if n1 != None:
        n.next = n1
    if n2 != None:
        n.next = n2
    return dummy.next
