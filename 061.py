#!/usr/bin/python3

def rotateRight(head, k):
    dummy = ListNode(0, head)
    node = head
    length = 0
    tail = dummy
    while node != None:
        tail = tail.next
        node = node.next
        length = length + 1

    if length == 0 or length == 1:
        return head

    k = k % length
    if k == 0:
        return head

    fast = head
    for i in range(0, k):
        fast = fast.next
    slow = dummy
    while fast != None:
        fast = fast.next
        slow = slow.next
    dummy.next = slow.next
    tail.next = head
    slow.next = None

    return dummy.next

