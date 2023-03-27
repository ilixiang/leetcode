#!/usr/bin/python3

from TreeNode import TreeNode

class BSTIterator:
    def __init(self, root):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self):
        revNode = self.stack.pop()
        cur = revNode.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return revNode.val

    def hasNext(self):
        return len(self.stack) != 0
