#!/usr/bin/python3

def lengthOfLIS(nums):
    d = [0] * len(nums)
    d[0] = nums[0]
    l = 1

    for i in range(1, len(nums)):
        num = nums[i]
        if num > d[l - 1]:
            d[l] = num
            l += 1
        else:
            low, high = 0, l - 1
            pos = -1
            while low <= high:
                mid = (low + high) >> 1
                if d[mid] >= num:
                    high = mid - 1
                else:
                    pos = mid
                    low = mid + 1
            d[pos + 1] = num
    return l

if __name__ == '__main__':
    assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

