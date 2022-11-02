#!/usr/bin/python3

def kthSamllest(root, k):
    cur = root
    stack = []
    while cur != None or len(stack) != 0:
        if cur != None:
            stack.append(cur)
            cur = cur.left
        else:
            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            cur = node.right
    return None


