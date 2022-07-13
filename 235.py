#!/usr/bin/python3

def lowestCommonAncestor(root, p, q):
    pVal = p.val
    qVal = q.val
    (left, right) = (pVal, qVal) if pVal < qVal else (qVal, pVal)
    node = root
    while node != None:
        val = node.val
        if left <= val and val <= right:
            return node
        elif right < val:
            node = node.left
        else:
            node = node.right
    return None

