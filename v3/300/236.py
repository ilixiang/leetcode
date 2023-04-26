#!/usr/bin/python3

def lowestCommonAncestor(root, p, q):

    def recursive(root):
        if not root:
            return None
        if root == p or root == q:
            return root
        
        leftRev = recursive(root.left)
        rightRev = recursive(root.right)
        if leftRev and rightRev:
            return root
        elif leftRev or rightRev:
            return leftRev if not rightRev else rightRev
        else:
            return None

    return recursive(root)
