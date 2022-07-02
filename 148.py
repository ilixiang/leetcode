#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def sortList(head):
    return mergeSort(head, None)

def mergeSort(start, end):
    if start == end or start.next == end:
        return start

    fast = start
    slow = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    mid = slow

    dummy = ListNode()
    left = mergeSort(start, mid)
    right = mergeSort(mid, end)
    current = dummy
    while left != mid and right != end:
        if left.val <= right.val:
            current.next = left
            current = left
            left = left.next
        else:
            current.next = right
            current = right
            right = right.next
    while left != mid:
        current.next = left
        current = left
        left = left.next
    while right != end:
        current.next = right
        current = right
        right = right.next
    current.next = end
    return dummy.next

node = sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
while node != None:
    print(node.val)
    node = node.next

