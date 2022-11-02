#!/usr/bin/python3

class MinStack:
    def __init__(self):
        self.length = 0
        self.minStack = []
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        if self.length == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[self.length - 1]))
        self.length += 1 

    def pop(self):
        if self.length == 0:
            return
        self.stack.pop()
        self.minStack.pop()
        self.length -= 1

    def top(self):
        if self.length == 0:
            return None
        return self.stack[self.length - 1]

    def getMin(self):
        if self.length == 0:
            return None
        return self.minStack[self.length - 1]


