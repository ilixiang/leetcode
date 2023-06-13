#!/usr/bin/python3

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self.cur = nestedList
        self.idx = 0

    def next(self):
        stack, cur, idx = self.stack, self.cur, self.idx
        while (idx == len(cur) and len(stack) != 0) or (idx < len(cur) and not cur[idx].isInteger()):
            while idx == len(cur) and len(stack) != 0:
                (cur, idx) = stack.pop()
                idx += 1
            while idx < len(cur) and not cur[idx].isInteger():
                stack.append((cur, idx))
                cur, idx = cur[idx].getList(), 0
        if idx < len(cur):
            self.cur, self.idx = cur, idx
            self.idx += 1
            return self.cur[self.idx - 1].getInteger()
        return None

    def hasNext(self):
        stack, cur, idx = self.stack, self.cur, self.idx
        while (idx == len(cur) and len(stack) != 0) or (idx < len(cur) and not cur[idx].isInteger()):
            while idx == len(cur) and len(stack) != 0:
                (cur, idx) = stack.pop()
                idx += 1
            while idx < len(cur) and not cur[idx].isInteger():
                stack.append((cur, idx))
                cur, idx = cur[idx].getList(), 0
        self.cur, self.idx = cur, idx
        return idx < len(cur)
