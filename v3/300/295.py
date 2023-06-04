#!/usr/bin/python3

import heapq

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
    
    def addNum(self, num):
        if len(self.right) != 0 and self.right[0] < num:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        else:
            heapq.heappush(self.left, -num)
            if len(self.left) == len(self.right) + 2:
                heapq.heappush(self.right, -1 * heapq.heappop(self.left))

    def findMedian(self):
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2
        return -1 * self.left[0]
