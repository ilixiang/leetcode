#!/usr/bin/python3

def getIntersectionNode(headA, headB):
    n1 = headA
    n2 = headB
    while n1 != None and n2 != None and n1 != n2:
        n1 = n1.next
        n2 = n2.next
    
    if n1 != None and n1 == n2:
        return n1

    if n1 == None and n2 == None:
        return None

    n1 = headB if n1 == None else n1
    n2 = headA if n2 == None else n2
    while n1 != None and n2 != None:
        n1 = n1.next
        n2 = n2.next
    
    n1 = headB if n1 == None else n1
    n2 = headA if n2 == None else n2
    while n1 != None and n2 != None and n1 != n2:
        n1 = n1.next
        n2 = n2.next
    
    if n1 == None or n2 == None:
        return None
    
    return n1


