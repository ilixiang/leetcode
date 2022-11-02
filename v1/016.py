#!/usr/bin/python3

def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[-1]
    left = 0
    while left < len(nums) - 2:
        mid, right = left + 1, len(nums) - 1
        while mid < right:
            tmpSum = nums[left] + nums[mid] + nums[right] 
            result = result if abs(tmpSum - target) > abs(result - target) else tmpSum
            if tmpSum < target:
                mid = mid + 1
            elif tmpSum > target:
                right = right - 1
            else:
                return result
        while left < len(nums) - 2 and nums[left] == nums[left + 1]:
            left = left + 1
        left = left + 1
    return result

print(threeSumClosest([0, 0, 0], 1))
print(threeSumClosest([-1, 2, 1, -4], 1))

