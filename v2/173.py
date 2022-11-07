#!/usr/bin/python3

from .TreeNode import TreeNode

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left
    
    def next(self):
        if len(self.stack) == 0:
            return None
        node = self.stack.pop()
        rev = node.val
        node = node.right
        while node != None:
            self.stack.append(node)
            node = node.left
        return rev
    
    def hasNext(self):
        return len(self.stack) != 0

