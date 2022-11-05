#!/usr/bin/python3

def zigzagLevelOrder(root):
    if root == None:
        return []
    
    s1 = [root]
    s2 = []
    leftFirst = True
    rev = []
    while len(s1) != 0:
        size = len(s1)
        tmp = [0] * size
        for i in range(0, size):
            n = s1.pop()
            tmp[i] = n.val
            first = n.left
            second = n.right
            if not leftFirst:
                first, second = second, first
            if first != None:
                s2.append(first)
            if second != None:
                s2.append(second)
        s1, s2 = s2, s1
        leftFirst = not leftFirst
        rev.append(tmp)
    return rev
