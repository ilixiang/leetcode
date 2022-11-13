#!/usr/bin/python3

def subarraySum(nums, k):
    rev = 0
    s = 0
    cumulativeSumMap = {0:1}
    for eIndex in range(0, len(nums)):
        s += nums[eIndex]
        diff = s - k
        diffCount = cumulativeSumMap.get(diff, 0)
        rev += diffCount
        cumulativeSumMap[s] = cumulativeSumMap.get(s, 0) + 1
    return rev


if __name__ == '__main__':
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,2,3], 3) == 2
