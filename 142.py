#!/usr/bin/python3

class ListNode:
    def __init__(self, x = 0, n = None):
        self.val = x
        self.next = n

def detectCycle(head):
    if head == None or head.next == None:
        return None
    fast = head.next.next
    slow = head.next
    while fast != None and fast.next != None and slow != fast:
        fast = fast.next.next
        slow = slow.next
    if slow != fast:
        return None
    fast = head
    print('FAST => %d, SLOW => %d'%(fast.val, slow.val))
    while fast != slow:
        print('FAST => %d, SLOW => %d'%(fast.val, slow.val))
        fast = fast.next
        slow = slow.next
    return slow

l = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
l.next.next.next.next = l.next
n = detectCycle(l)
print(n.val)

