#!/usr/bin/python3

def majorityElement(nums):
    rev = nums[0]
    voteNum = 1
    for i in range(1, len(nums)):
        if rev == nums[i]:
            voteNum += 1
        else:
            if voteNum == 0:
                rev = nums[i]
                voteNum += 1
            else:
                voteNum -= 1
    return rev

