#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def partition(head, x):
    if head == None:
        return head
    additionHead = ListNode(0, head)
    left = additionHead
    rightPrevious = additionHead
    right = rightPrevious.next 
    while right != None:
        if right.val < x:
            if right != left.next:
                rightPrevious.next = right.next
                right.next = left.next
                left.next = right
                left = left.next
                right = rightPrevious.next
            else:
                left = left.next
                rightPrevious = rightPrevious.next
                right = rightPrevious.next
        else:
            rightPrevious = rightPrevious.next
            right = rightPrevious.next
    return additionHead.next
    
head = ListNode(1, ListNode(4, ListNode(3, ListNode(0, ListNode(2, ListNode(5, ListNode(2)))))))
head = partition(head, 3)
while head != None:
    print(head.val)
    head = head.next

