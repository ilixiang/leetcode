#!/usr/bin/python3

def majorityElement(nums):
    majority = None
    count = 0
    for num in nums:
        if count == 0:
            majority = num
            count += 1
        else:
            if majority == num:
                count += 1
            else:
                count -= 1
    return majority
