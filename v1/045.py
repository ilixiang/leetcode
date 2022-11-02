#!/usr/bin/python3

# Greedy
def jump(nums):
    if len(nums) == 1:
        return 0
    for index in range(0, len(nums)):
        nums[index] = index + nums[index]
    maxReachableIndex = nums[0]
    lastReachableIndex = 0
    step = 1
    while maxReachableIndex < len(nums) - 1:
        newReachableIndex = maxReachableIndex
        for index in range(lastReachableIndex + 1, maxReachableIndex + 1):
            print('INDEX => %d'%(index))
            newReachableIndex = max(newReachableIndex, nums[index])
        lastReachableIndex = maxReachableIndex
        maxReachableIndex = newReachableIndex
        print('MAX_REACHABLE_INDEX => %d'%(maxReachableIndex))
        step = step + 1
    return step

print(jump([2, 3, 1, 1, 4]))
print(jump([2, 1, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))

