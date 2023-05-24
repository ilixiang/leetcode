#!/usr/bin/python3

class PeekingIterator:
    def __init__(self, iterator):
        self.cur = None
        self.iterator = iterator
    
    def peek(self):
        if self.cur:
            return self.cur
        if not self.iterator.hasNext():
            return None
        self.cur = self.iterator.next()
        return self.cur
    
    def next(self):
        if not self.cur and not self.iterator.hasNext():
            return None
        if self.cur:
            rev = self.cur
            self.cur = None
            return rev
        return self.iterator.next()
    
    def hasNext(self):
        return self.cur != None or self.iterator.hasNext()

