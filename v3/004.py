#!/usr/bin/python3

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) == 0 and len(nums2) == 0:
        return None

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    MAX_NUM = 10 ** 6
    MIN_NUM = -1 * 10 ** 6
    total = len(nums1) + len(nums2)
    left = total // 2
    if len(nums1) == 0:
        return float(nums2[left]) if len(nums2) & 1 == 1 else ((nums2[left - 1] + nums2[left]) / 2)
    
    l1, r1 = 0, len(nums1)
    while l1 <= r1:
        m1 = (l1 + r1) // 2
        m2 = left - m1

        if m1 > 0 and m2 < len(nums2) and nums1[m1 - 1] > nums2[m2]:
            r1 = m1
        elif m2 > 0 and m1 < len(nums1) and nums2[m2 - 1] > nums1[m1]:
            l1 = m1 + 1
        else:
            if total & 1 == 1:
                return float(min(nums1[m1] if m1 != len(nums1) else MAX_NUM, nums2[m2] if m2 != len(nums2) else MAX_NUM))
            else:
                return (max(nums1[m1 - 1] if m1 != 0 else MIN_NUM, nums2[m2 - 1] if m2 != 0 else MIN_NUM)\
                        + min(nums1[m1] if m1 != len(nums1) else MAX_NUM, nums2[m2] if m2 != len(nums2) else MAX_NUM)) / 2

    return None

