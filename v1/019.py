#!/usr/bin/python3

class ListNode(object):
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def removeNthFromEnd(head, n):
    additionHeadNode = ListNode(0, head)
    previousStartNode = additionHeadNode
    endNode = previousStartNode
    for i in range(0, n):
        if endNode == None:
            return head
        endNode = endNode.next
    startNode = head
    while endNode.next != None:
        previousStartNode = startNode
        startNode = startNode.next
        endNode = endNode.next
    previousStartNode.next = startNode.next
    return additionHeadNode.next 
