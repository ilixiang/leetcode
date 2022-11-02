#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def reorderList(head):
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy
    rightNodeCount = 0
    while fast != None and fast.next != None:
        slow = slow.next
        rightNodeCount = rightNodeCount + 1
        fast = fast.next.next
    if fast == None:
        rightNodeCount = rightNodeCount - 1

    right = slow.next
    if right == None:
        return

    slow.next = None
    previousNode = right
    while previousNode.next != None:
        curNode = previousNode.next
        previousNode.next = curNode.next
        curNode.next = right
        right = curNode

    left = head
    curNode = dummy
    while left != None and right != None:
        curNode.next = left
        left = left.next
        curNode.next.next = right
        right = right.next
        curNode = curNode.next.next
    if left != None:
        curNode.next = left

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(node)
while node != None:
    print(node.val)
    node = node.next
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorderList(node)
while node != None:
    print(node.val)
    node = node.next

