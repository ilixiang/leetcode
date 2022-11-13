#!/usr/bin/python3

def maxSlidingWindow(nums, k):
    rev = [0] * (len(nums) + 1 - k)
    deque = []
    for i in range(0, k):
        while len(deque) != 0 and nums[deque[-1]] < nums[i]:
            deque.pop()
        deque.append(i)
    rev[0] = nums[deque[0]]

    left = 1
    right = k
    while right < len(nums):
        if len(deque) != 0 and deque[0] < left:
            deque.pop(0)

        num = nums[right]
        while len(deque) != 0 and nums[deque[-1]] < num:
            deque.pop()
        deque.append(right)
        rev[left] = nums[deque[0]]
        left += 1
        right += 1
    return rev
