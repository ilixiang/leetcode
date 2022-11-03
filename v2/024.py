#!/usr/bin/python3

from .ListNode import ListNode

def swapPairs(head):
    dummy = ListNode(0, head)
    pairPrev = dummy
    prevNode = dummy
    while prevNode.next != None:
        if prevNode == pairPrev:
            prevNode = prevNode.next
            continue
        node = prevNode.next
        prevNode.next = node.next
        node.next = pairPrev.next
        pairPrev.next = node

        pairPrev = prevNode
    return dummy.next
