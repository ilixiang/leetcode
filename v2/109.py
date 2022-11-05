#!/usr/bin/python3

from .ListNode import ListNode
from .TreeNode import TreeNode

def sortedListToBST(head):
    def sortedListToBSTRecursive(start, end):
        if start == end:
            return None
        
        slow = fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        
        left = sortedListToBSTRecursive(start, slow)
        right = sortedListToBSTRecursive(slow.next, end)
        return TreeNode(slow.val, left, right)
    return sortedListToBSTRecursive(head, None)
