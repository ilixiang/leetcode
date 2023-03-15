#!/usr/bin/python3

from ListNode import ListNode
from TreeNode import TreeNode

def sortedListToBST(head):
    def buildTree(left, right):
        if left == right:
            return None

        slow = fast = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        
        return TreeNode(slow.val, buildTree(left, slow),  buildTree(slow.next, right))
    return buildTree(head, None)
