#!/usr/bin/python3

def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    for left in range(0, len(nums) - 2):
        if left > 0 and nums[left] == nums[left - 1]:
            continue
        mid, right = left + 1, len(nums) - 1
        diff = -1 * nums[left]
        while mid < right:
            if nums[mid] + nums[right] > diff:
                right = right - 1
            elif nums[mid] + nums[right] < diff:
                mid = mid + 1
            else:
                result.append([nums[left], nums[mid], nums[right]])
                mid = mid + 1
                right = right - 1
                while mid < right and nums[mid] == nums[mid - 1] and nums[right] == nums[right + 1]:
                    mid = mid + 1
                    right = right - 1
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))
        


