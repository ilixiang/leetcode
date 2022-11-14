#!/usr/bin/python3

def minCameraCover(root):
    def recursive(root):
        left, right = root.left, root.right

        if left == None and right == None:
            return (1, 1, 0)
        
        if left == None or right == None:
            child = left if right == None else right
            childRev = recursive(child)
            return (1 + childRev[2], min(childRev[0], 1 + childRev[2]), min(childRev[1], 1 + childRev[2]))

        leftRev = recursive(left)
        rightRev = recursive(right)

        return (
            1 + leftRev[2] + rightRev[2],
            min(1 + leftRev[2] + rightRev[2], leftRev[0] + rightRev[1], leftRev[1] + rightRev[0]),
            min(1 + leftRev[2] + rightRev[2], leftRev[1] + rightRev[1])
        )
    return recursive(root)[1]