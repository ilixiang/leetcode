#!/usr/bin/python3

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    odd = (len(nums1) + len(nums2)) % 2 == 1

    left = 0
    right = len(nums1)
    while left < right:
        mid1 = (left + right) // 2
        mid2 = (len(nums2) + len(nums1)) // 2 - mid1
        if mid1 - 1 >= 0 and mid2 < len(nums2) and nums2[mid2] < nums1[mid1 - 1]:
            right = mid1
        elif mid2 - 1 >= 0 and nums2[mid2 - 1] > nums1[mid1]:
            left = mid1 + 1
        else:
            break
    
    mid1 = (left + right) // 2
    mid2 = (len(nums2) + len(nums1)) // 2 - mid1

    leftVal = 0
    rightVal = 0
    if mid1 == 0:
        leftVal = nums2[mid2 - 1]
    elif mid2 == 0:
        leftVal = nums1[mid1 - 1]
    else:
        leftVal = max(nums1[mid1 - 1], nums2[mid2 - 1])
    
    if mid1 == len(nums1):
        rightVal = nums2[mid2]
    elif mid2 == len(nums2):
        rightVal = nums1[mid1]
    else:
        rightVal = min(nums1[mid1], nums2[mid2])
    
    if odd:
        return float(rightVal)
    else:
        return (leftVal + rightVal) / 2