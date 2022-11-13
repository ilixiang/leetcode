#!/usr/bin/python3

import heapq

class MedianFinder:
    
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def addNum(self, num):
        if len(self.maxHeap) == 0 or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return (float)(-self.maxHeap[0])
