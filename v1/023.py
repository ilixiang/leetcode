#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def mergeKLists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]

    return mergeKRangedLists(lists, 0, len(lists))

def mergeKRangedLists(lists, start, end):
    if start >= end:
        return None
    if start == end - 1:
        return lists[start]
    mid = (start + end) // 2
    left = mergeKRangedLists(lists, start, mid)
    right = mergeKRangedLists(lists, mid, end)
    return mergeList(left, right)
    
def mergeList(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    head = ListNode()
    n = head
    n1, n2 = l1, l2
    while n1 != None and n2 != None:
        if n1.val > n2.val:
            n.next = n2
            n2 = n2.next
        else:
            n.next = n1
            n1 = n1.next
        n = n.next
    if n1 == None:
        n.next = n2
    else:
        n.next = n1
    return head.next

l = mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
while l != None:
    print(l.val)
    l = l.next

