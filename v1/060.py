#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

def getPermutation(n, k):
    if k == 1:
        return ''.join(map(lambda i: str(i), range(1, n + 1)))
    arr = [None] * n

    unset = 1
    fac = 1
    while fac < k:
        fac = fac * unset
        unset = unset + 1
    unset = unset - 1
    for i in range(0, n - unset):
        arr[i] = str(i + 1)

    dummy = ListNode()
    tail = dummy
    for i in range(n - unset + 1, n + 1):
        tail.next = ListNode(str(i))
        tail = tail.next

    fac = fac // unset
    unset = unset - 1
    k = k - 1
    while k != 0:
        pos = k // fac
        k = k % fac
        previousNode = dummy
        node = dummy.next
        for i in range(0, pos):
            previousNode = previousNode.next
            node = node.next
        previousNode.next = node.next
        arr[n - unset - 1] = node.val
        fac = fac // unset
        unset = unset - 1

    node = dummy.next
    while node != None:
        arr[n - unset - 1] = node.val
        node = node.next
        unset = unset - 1
    return ''.join(arr)

print(getPermutation(4, 9))
print(getPermutation(3, 1))
print(getPermutation(3, 5))

