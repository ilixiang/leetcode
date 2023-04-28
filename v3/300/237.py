#!/usr/bin/python3

from ListNode import ListNode

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
