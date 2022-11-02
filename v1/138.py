#!/usr/bin/python3

def copyRandomList(head):
    if head == None:
        return None

    node = head
    while node != None:
        nextNode = node.next
        dupNode = Node(node.val, nextNode, None)
        node.next = dupNode
        node = nextNode

    node = head
    dupNode = head.next
    while node != None:
        if node.random:
            dupNode.random = node.random.next
        node = dupNode.next
        if node != None:
            dupNode = dupNode.next.next

    node = head
    dummy = Node(0, None)
    previousDupNode = dummy
    while node != None:
        dupNode = node.next
        previousDupNode.next = dupNode
        previousDupNode = dupNode
        node.next = dupNode.next
        node = node.next

    return dummy.next
