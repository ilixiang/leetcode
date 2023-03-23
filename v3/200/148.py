#!/usr/bin/python3

from ListNode import ListNode

def sortList(head):
    def recursive(head, tail):
        if head == tail:
            return None
        if head.next == tail:
            head.next = None
            return head
        
        slow, fast = head.next, head.next.next
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        
        l1 = recursive(head, slow)
        l2 = recursive(slow, tail)

        prev = dummy = ListNode()
        n1, n2 = l1, l2
        while n1 and n2:
            if n1.val < n2.val:
                prev.next = n1
                n1 = n1.next
            else:
                prev.next = n2
                n2 = n2.next
            prev = prev.next
        if n1:
            prev.next = n1
        if n2:
            prev.next = n2
        return dummy.next
    return recursive(head, None)

        
