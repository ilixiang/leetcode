#!/usr/bin/python3

def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    
    length = 0
    triplet = [0] * 3
    for num in nums:
        if length == 3:
            break
        i = 0
        while triplet[i] < num and i < length:
            i += 1
        triplet[i] = num
        if i == length:
            length += 1
    return length == 3
