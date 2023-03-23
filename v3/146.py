class CacheNode:
    def __init__(self, key = 0, val = 0, p = None, n = None):
        self.key = key
        self.val = val
        self.prev = p
        self.next = n

class LRUCache:
    def __init__(self, capacity):
        self.m = {}
        self.remainCapacity = capacity
        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.m.get(key, None)
        if not node:
            return -1
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        node.prev.next = node
        return node.val

    def put(self, key, value):
        node = self.m.get(key, None)
        if not node:
            node = CacheNode(key, value, self.tail.prev, self.tail)
            node.prev.next = node
            node.next.prev = node
            self.m[key] = node
            self.remainCapacity -= 1
        else:
            node.val = value
        
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        node.prev.next = node

        if self.remainCapacity < 0:
            lastNode = self.tail.prev
            self.tail.prev = lastNode.prev
            lastNode.prev.next = self.tail
            del self.m[lastNode.key]
            self.remainCapacity += 1
