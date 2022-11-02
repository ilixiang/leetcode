#!/usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getInsersectionNode(headA, headB):
    nodeA = headA
    nodeB = headB

    countA = 0
    countB = 0
    while nodeA != None:
        nodeA = nodeA.next
        countA = countA + 1
    while nodeB != None:
        nodeB = nodeB.next
        countB = countB + 1

    longListNode = None
    shortListNode = None
    if countA > countB:
        longListNode, shortListNode = headA, headB
    else:
        longListNode, shortListNode = headB, headA

    for i in range(0, abs(countA - countB)):
        longListNode = longListNode.next

    while longListNode != shortListNode:
        longListNode = longListNode.next
        shortListNode = shortListNode.next

    return longListNode

