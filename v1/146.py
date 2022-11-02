#!/usr/bin/python3

class CacheNode:
    def __init__(self, key, val, prev = None, n = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = n

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dummyHead = CacheNode(0, 0)
        self.dummyTail = CacheNode(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def get(self, key):
        node = self.cache.get(key)
        if node == None:
            return -1
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = self.dummyHead.next
        node.prev = self.dummyHead
        node.next.prev = node
        self.dummyHead.next = node
        return node.val

    def put(self, key, value):
        node = self.cache.get(key)
        if node == None:
            node = CacheNode(key, value)
            self.cache[key] = node
        else:
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
            
        node.prev = self.dummyHead
        node.next = self.dummyHead.next
        self.dummyHead.next = node
        node.next.prev = node
        if len(self.cache) > self.capacity:
            evitNode = self.dummyTail.prev
            self.dummyTail.prev = evitNode.prev
            evitNode.prev.next = self.dummyTail
            del self.cache[evitNode.key]

c = LRUCache(2)
c.put(1,1)
c.put(2,2)
print(c.get(1))
c.put(3,3)
print(c.get(2))
c.put(4,4)
print(c.get(1))
print(c.get(3))
print(c.get(4))
