#!/usr/bin/python3

class Heap:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)
    
    def heapify(self, i):
        size = len(self.storage)
        while i <= (size - 2) // 2:
            left = 2 * i + 1
            right = 2 * i + 2
            minChild = left if right >= size or self.storage[left] < self.storage[right] else right
            self.storage[i], self.storage[minChild] = self.storage[minChild], self.storage[i]
            i = minChild
    
    def min(self):
        if len(self.storage) == 0:
            return None
        rev = self.storage[0]
        self.storage[0] = self.storage[-1]
        del self.storage[-1]
        self.heapify(0)
        return rev
        
    def push(self, num):
        self.storage.append(num)
        i = len(self.storage) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.storage[parent] <= self.storage[i]:
                break
            self.storage[parent], self.storage[i] = self.storage[i], self.storage[parent]
            i = parent
            

def furthestBuilding(heights, bricks, ladders):
    length = len(heights)
    heap = Heap()
    for i in range(0, length - 1):
        heightDiff = heights[i + 1] - heights[i]
        if heightDiff > 0:
            heap.push(heightDiff)
        
        if heap.size() > ladders:
            bricks -= heap.min()
            if bricks < 0:
                return i
    return length - 1

if __name__ == '__main__':
    assert furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4
    assert furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7

