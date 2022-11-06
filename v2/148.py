#!/usr/bin/python3

from .ListNode import ListNode

def sortList(head):

    def mergeSortList(head):
        if head == None or head.next == None:
            return head
        
        slow = head
        fast = head.next.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        l1 = mergeSortList(head)
        l2 = mergeSortList(mid)
        dummy = ListNode(0)
        prev = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        if l1 != None:
            prev.next = l1
        if l2 != None:
            prev.next = l2
        return dummy.next

    return mergeSortList(head)
