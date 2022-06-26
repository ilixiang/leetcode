#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def reverseBetween(head, left, right):
    if left == right:
        return head

    dummy = ListNode(0, head)
    leftPreviousNode = dummy
    leftNode = head
    rightNextNode = head

    for step in range(1, left):
        leftPreviousNode = leftPreviousNode.next
    leftNode = leftPreviousNode.next
    for step in range(0, right):
        rightNextNode = rightNextNode.next

    current = leftNode
    while current != rightNextNode:
        if current != leftPreviousNode.next:
            leftNode.next = current.next
            current.next = leftPreviousNode.next
            leftPreviousNode.next = current
        current = leftNode.next
    return dummy.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reverseBetween(head, 2, 4)
while head != None:
    print(head.val)
    head = head.next

