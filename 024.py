#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def swapPairs(head):
    if head == None or head.next == None:
        return head

    leftPrevious = ListNode() 
    leftPrevious.next = head
    head = leftPrevious
    left = leftPrevious.next
    right = left.next
    while left != None and right != None:
        leftPrevious.next = right
        left.next = right.next
        right.next = left

        leftPrevious = left
        left = left.next 
        right = None if left == None else left.next
    return head.next

l = swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
n = l
while n != None:
    print(n.val)
    n = n.next
