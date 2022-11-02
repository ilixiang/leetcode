#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def deleteDuplicates(head):
    dummy = ListNode(0, head)
    first = head
    current = head
    while current != None:
        if first.val != current.val:
            first.next = current
            first = current
        current = current.next

    if first != None:
        first.next = None
    return dummy.next

h = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
deleteDuplicates(h)
while h != None:
    print(h.val)
    h = h.next


