#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def reverseList(head):
    if head == None or head.next == None:
        return head
    dummy = ListNode(0, head)
    current = head.next
    while current != None:
        head.next = current.next
        current.next = dummy.next
        dummy.next = current
        current = head.next
    return dummy.next


