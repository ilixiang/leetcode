#!/usr/bin/python3

def majorityElement(nums):
    m = {}
    for num in nums:
        count = m.get(num, 0)
        m[num] = count + 1
    
    return list(filter(lambda n: m[n] > len(nums) // 3, m))
