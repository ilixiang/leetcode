#!/usr/bin/python3

def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) >> 1
        if nums[m] == target:
            return True

        if nums[l] < nums[r]:
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif nums[l] > nums[r]:
            if nums[m] <= nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        else:
            while l <= r and nums[l] == nums[r]:
                l += 1
    return False
