#!/usr/bin/python3

from TreeNode import TreeNode

def zigzagLevelOrder(root):
    if root == None:
        return []

    s1 = [root]
    s2 = []
    rev = []
    level = 0
    while len(s1) != 0:
        c = len(s1)
        tmp = [0] * c
        for i in range(c):
            n = s1.pop()
            tmp[i] = n.val
            if level & 1 == 0:
                if n.left:
                    s2.append(n.left)
                if n.right:
                    s2.append(n.right)
            else:
                if n.right:
                    s2.append(n.right)
                if n.left:
                    s2.append(n.left)
        rev.append(tmp)
        level += 1
        s1, s2 = s2, s1
    return rev
