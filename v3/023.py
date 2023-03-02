#!/usr/bin/python3

from ListNode import ListNode

def mergeKSortedLists(lists):
    def merge(i, j):
        if i > j:
            return None
        if i == j:
            return lists[i]
        
        m = (i + j) // 2
        n1 = merge(i, m)
        n2 = merge(m + 1, j)

        cur = dummy = ListNode()
        while n1 != None and n2 != None:
            if n1.val < n2.val:
                cur.next = n1
                cur = n1
                n1 = n1.next
            else:
                cur.next = n2
                cur = n2
                n2 = n2.next
        cur.next = n1 if n2 == None else n2
        return dummy.next
    return merge(0, len(lists) - 1)
        