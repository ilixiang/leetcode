#!/usr/bin/python3

def fourSum(nums, target):
    nums.sort()

    first = 0
    rev = []
    while first < len(nums) - 3:
        if first != 0 and nums[first] == nums[first - 1]:
            first += 1
            continue
        
        second = first + 1
        while second < len(nums) - 2:
            if second != first + 1 and nums[second] == nums[second - 1]:
                second += 1
                continue
            
            third, fourth = second + 1, len(nums) - 1
            while third < fourth:
                s = nums[first] + nums[second] + nums[third] + nums[fourth]
                if s == target:
                    rev.append([nums[first], nums[second], nums[third], nums[fourth]])
                    third += 1
                    while third < fourth and nums[third] == nums[third - 1]:
                        third += 1
                elif s < target:
                    third += 1
                else:
                    fourth -= 1
            second += 1
        first += 1
    return rev
