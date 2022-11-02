#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def insertionSortList(head):
    dummy = ListNode(0, head)
    end = dummy
    curNode = head
    while curNode != None:
        previousNode = dummy
        while previousNode != end and previousNode.next.val < curNode.val:
            previousNode = previousNode.next
        if previousNode == end:
            end = end.next
        else:
            end.next = curNode.next
            curNode.next = previousNode.next
            previousNode.next = curNode
        curNode = end.next
    return dummy.next

node = insertionSortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
while node != None:
    print(node.val)
    node = node.next

