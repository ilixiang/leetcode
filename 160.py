#!/usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getInsersectionNode(headA, headB):
    nodeA = headA
    nodeB = headB
    while nodeA != None and nodeB != None:
        if nodeA == nodeB:
            return nodeA
        nodeA = nodeA.next
        nodeB = nodeB.next

    longListHead = None
    shortListHead = None
    longListNode = None
    shortListNode = None
    if nodeA is None:
        longListHead = headB
        longListNode = nodeB
        shortListHead = headA
        shortListNode = nodeA
    else:
        longListHead = headB
        longListNode = nodeB
        shortListHead = headA
        shortListNode = nodeA

    shortListNode = shortListHead
    while longListNode != None:
        shortListNode = shortListNode.next
        longListNode = longListNode.next

    longListNode = longListHead
    while longListNode != shortListNode:
        longListNode = longListNode.next
        shortListNode = shortListNode.next

    return longListNode

