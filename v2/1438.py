#!/usr/bin/python3

def longestSubarray(nums, limit):
    decreasingStack = []
    increasingStack = []

    rev = 0
    cur = 0
    for i in range(0, len(nums)):
        num = nums[i]
        while len(decreasingStack) != 0 and nums[decreasingStack[-1]] < num:
            decreasingStack.pop()
        decreasingStack.append(i)
        
        while len(increasingStack) != 0 and nums[increasingStack[-1]] > num:
            increasingStack.pop()
        increasingStack.append(i)

        if abs(nums[decreasingStack[0]] - nums[increasingStack[0]]) <= limit:
            cur += 1
        else:
            rev = max(rev, cur)
            if len(decreasingStack) < len(increasingStack):
                while abs(nums[decreasingStack[0]] - nums[increasingStack[0]]) > limit:
                    cur = i - increasingStack.pop(0)
            else:
                while abs(nums[decreasingStack[0]] - nums[increasingStack[0]]) > limit:
                    cur = i - decreasingStack.pop(0)
    rev = max(rev, cur)
    return rev
