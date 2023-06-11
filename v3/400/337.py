#!/usr/bin/python3

from TreeNode import TreeNode


def rob(root):
    def recursive(root):
        if not root:
            return (0, 0)
        leftRev = recursive(root.left)
        rightRev = recursive(root.right)
        return (root.val + leftRev[1] + rightRev[1], max(leftRev) + max(rightRev))
    rev = recursive(root)
    return max(rev)
