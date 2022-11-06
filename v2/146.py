#!/usr/bin/python3

class CacheNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.head = CacheNode(None, None)
        self.tail = CacheNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def get(self, key):
        node = self.storage.get(key)
        if node != None:
            if node.prev != self.head:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = self.head
                node.next = self.head.next
                node.prev.next = node
                node.next.prev = node
            return node.val
        return -1

    def put(self, key, value):
        node = None
        if key in self.storage:
            node = self.storage[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = CacheNode(key, value)
            if self.capacity == len(self.storage):
                evictNode = self.tail.prev
                evictNode.prev.next = evictNode.next
                evictNode.next.prev = evictNode.prev
                del self.storage[evictNode.key]
            self.storage[key] = node
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        node.prev.next = node

