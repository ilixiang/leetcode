#!/usr/bin/python3

def maxProduct(nums):
    previous = (0, 0) if nums[0] == 0 else ((nums[0], None) if nums[0] > 0 else (0, nums[0]))
    result = nums[0]
    for i in range(1, len(nums)):
        previous = generate(nums[i], previous[0], previous[1])
        if previous[0] != None:
            result = max(result, previous[0])
    return result

def generate(num, previousMax, previousMin):
    currentMax = None
    currentMin = None
    if num == 0:
        return (0, 0)
    elif num > 0:
        return (num if (previousMax == None or previousMax == 0) else (num * previousMax), None if (previousMin == None or previousMin == 0) else (num * previousMin))
    else:
        return (None if (previousMin == None or previousMin == 0) else (num * previousMin),  num if (previousMax == None or previousMax == 0) else (num * previousMax))

print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
