#!/usr/bin/python3

def isPalindrome(head):
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    center = slow
    cur = slow.next
    if cur == None:
        return True

    while cur.next != None:
        node = cur.next
        cur.next = node.next
        node.next = center.next
        center.next = node

    left = head
    right = center.next
    while right != None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

        

