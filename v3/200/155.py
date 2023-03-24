#!/usr/bin/python3

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        self.minStack.pop()
        return self.stack.pop()
    
    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self):
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]
