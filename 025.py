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
    end = startPrevious
    endNext = end.next
    
    while True:
        step = 0
        while step < k and endNext != None:
            end = end.next
            endNext = end.next
            step = step + 1
        if step < k:
            return additionHead.next

        while start.next != endNext:
            tmp = start.next
            start.next = start.next.next
            tmp.next = startPrevious.next
            startPrevious.next = tmp

        startPrevious = start
        start = startPrevious.next
        end = startPrevious
        endNext = end.next


h = reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while h != None:
    print(h.val)
    h = h.next
