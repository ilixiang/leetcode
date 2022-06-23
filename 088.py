#!/usr/bin/python3

def merge(nums1, m, nums2, n):
    i1, i2 = m - 1, n - 1
    rIndex = m + n - 1
    while i1 >= 0 and i2 >= 0:
        if nums1[i1] > nums2[i2]:
            nums1[rIndex] = nums1[i1]
            i1 = i1 - 1
        else:
            nums1[rIndex] = nums2[i2]
            i2 = i2 - 1
        rIndex = rIndex - 1

    while i2 >= 0:
        nums1[rIndex] = nums2[i2]
        i2 = i2 - 1
        rIndex = rIndex - 1
    return nums1

print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1, 2, 3], 3, [], 0))
print(merge([0, 0, 0], 0, [1, 2, 3], 3))

