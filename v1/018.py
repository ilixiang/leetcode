#!/usr/bin/python3

def fourSum(nums, target):
    if len(nums) < 4:
        return []
    nums.sort()
    result = []
    first = 0
    while first < len(nums) - 3:
        if first > 0: 
            while first < len(nums) - 3 and nums[first] == nums[first - 1]:
                first = first + 1
        second = first + 1
        while second < len(nums) - 2:
            if second > first + 1:
                while second < len(nums) - 2 and nums[second] == nums[second - 1]:
                    second = second + 1
            third, fourth = second + 1, len(nums) - 1
            while third < fourth:
                print('FIRST => %d, SECOND => %d, THIRD => %d, FOURTH => %d'%(first, second, third, fourth))
                tmpSum = nums[first] + nums[second] + nums[third] + nums[fourth]
                if tmpSum < target:
                    third = third + 1
                elif tmpSum > target:
                    fourth = fourth - 1
                else:
                    result.append([nums[first], nums[second], nums[third], nums[fourth]])
                    third = third + 1
                    fourth = fourth - 1
                    while third < fourth and nums[third] == nums[third - 1] and nums[fourth] == nums[fourth + 1]:
                        third = third + 1
                        fourth = fourth - 1
            second = second + 1
        first = first + 1
    return result

print(fourSum([2, 2, 2, 2, 2], 8))
print(fourSum([1, 0, -1, 0, -2, 2], 0))
print(fourSum([-2, -1, -1, 1, 1, 2, 2], 0))

