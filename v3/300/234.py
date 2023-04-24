#!/usr/bin/python3

from ListNode import ListNode

def isPalindrome(head):
    slow = fast = ListNode(0, head)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first = slow
    last = slow.next
    if not last:
        return True

    while last.next:
        node = last.next
        last.next = node.next
        node.next = first.next
        first.next = node
    
    left, right = head, first.next
    while right and left.val == right.val:
        left = left.next
        right = right.next
    return not right

