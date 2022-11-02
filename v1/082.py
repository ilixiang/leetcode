#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def deleteDuplicates(head):
    dummy = ListNode(0, head)
    previous = dummy
    first = head
    current = head
    while current != None:
        if first.val != current.val:
            if first.next != current:
                previous.next = current
            else:
                previous = first
            first = current
        else:
            current = current.next

    if first != None and first.next != None:
        previous.next = None
    return dummy.next

h = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
deleteDuplicates(h)
while h != None:
    print(h.val)
    h = h.next

