#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def reverseKGroup(head, k):
    if k == 1:
        return head
    additionHead = ListNode(0, head)
    startPrevious = additionHead
    start = head
    
    while start != None:
        step = 1
        while step < k and start.next != None:
            tmp = start.next
            start.next = start.next.next
            tmp.next = startPrevious.next
            startPrevious.next = tmp
            step = step + 1

        if step < k:
            start = startPrevious.next
            while start.next != None:
                tmp = start.next
                start.next = start.next.next
                tmp.next = startPrevious.next
                startPrevious.next = tmp
                step = step + 1
            return additionHead.next

        startPrevious = start
        start = startPrevious.next
    return additionHead.next

