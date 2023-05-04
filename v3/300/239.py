#!/usr/bin/python3

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    rev = [0] * (len(nums) - k + 1)
    for i in range(len(nums)):
        while len(dq) > 0 and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            rev[i + 1 - k] = nums[dq[0]]
        if dq[0] <= i + 1 - k:
            dq.popleft()
    return rev
