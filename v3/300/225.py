#!/usr/bin/python3

class Mystack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if len(self.q1) == 0:
            return None
        while len(self.q1) != 1:
            self.q2.append(self.q1.pop(0))
        rev = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return rev

    def top(self):
        if len(self.q1) == 0:
            return None
        while len(self.q1) != 1:
            self.q2.append(self.q1.pop(0))
        rev = self.q1.pop(0)
        self.q2.append(rev)
        self.q1, self.q2 = self.q2, self.q1
        return rev

    def empty(self):
        return len(self.q1) == 0
