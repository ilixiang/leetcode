#!/usr/bin/python3

def deleteNode(node):
    prev = node
    cur = node.next
    while cur.next != None:
        prev.val = cur.val
        prev = cur
        cur = cur.next
    prev.val = cur.val
    prev.next = None

