#!/usr/bin/python3

def sortedListToBST(head):
    return buildBST(head, None)

def buildBST(left, right):
    if left == right:
        return None

    if left.next == right:
        return TreeNode(left.val)
    
    slow = left
    fast = left
    while slow != right and fast != right and fast.next != right:
        slow = slow.next
        fast = fast.next.next

    return TreeNode(slow.val, buildBST(left, slow), buildBST(slow.next, right))

