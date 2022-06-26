#!/usr/bin/python3

def search(nums, target):
    low, high = 0, len(nums)
    mid = (low + high) // 2
    while low < high:
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            if nums[low] < nums[mid] or nums[mid] > nums[high - 1]:
                if nums[low] == target:
                    return True
                elif nums[low] < target:
                    high = mid
                else:
                    low = mid + 1
            elif nums[low] > nums[mid] or nums[mid] < nums[high - 1]:
                high = mid
            else:
                index = low
                while index < high:
                    if nums[index] == target:
                        return True
                    index = index + 1
                return False
            mid = (low + high) // 2
        else:
            if nums[low] < nums[mid] or nums[mid] > nums[high - 1]:
                low = mid + 1
            elif nums[low] > nums[mid] or nums[mid] < nums[high - 1]:
                if nums[high - 1] == target:
                    return True
                elif nums[high - 1] < target:
                    high = mid 
                else:
                    low = mid + 1
            else:
                index = low
                while index < high:
                    if nums[index] == target:
                        return True
                    index = index + 1
                return False
            mid = (low + high) // 2
    return False

print(search([2,5,6,0,0,1,2], 0))
print(search([2,5,6,0,0,1,2], 3))
print(search([1,3], 2))

