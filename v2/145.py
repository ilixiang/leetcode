#!/usr/bin/python3

def postorderTraversal(root):
    if root == None:
        return []

    s1 = [root]
    rev = []
    while len(s1) != 0:
        node = s1.pop()
        rev.append(node.val)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    rev.reverse()
    return rev
