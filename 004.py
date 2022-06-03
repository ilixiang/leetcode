#!/usr/bin/python3

def findMedianSortedArrays(nums1, nums2):
    activeNums = nums1 if len(nums1) < len(nums2) else nums2
    passiveNums = nums2 if len(nums1) < len(nums2) else nums1
    odd = (len(nums1) + len(nums2)) % 2 == 1
    medianPosition = (len(nums1) + len(nums2)) // 2
    right = len(activeNums)
    left = 0
    activeMid = (left + right) // 2
    passiveMid = medianPosition - activeMid
    while not ((activeMid == 0 or (activeNums[activeMid - 1] <= passiveNums[passiveMid])) and (activeMid == len(activeNums) or (activeNums[activeMid] >= passiveNums[passiveMid - 1]))):
        if not (activeMid == 0 or (activeNums[activeMid - 1] <= passiveNums[passiveMid])):
            right = activeMid
        else:
            left = activeMid + 1
        activeMid = (left + right) // 2
        passiveMid = medianPosition - activeMid

    maxLeft = passiveNums[passiveMid - 1] if activeMid == 0 else (activeNums[activeMid - 1] if passiveMid == 0 else max(activeNums[activeMid - 1], passiveNums[passiveMid - 1]))
    minRight = passiveNums[passiveMid] if activeMid == len(activeNums) else (activeNums[activeMid] if passiveMid == len(passiveNums) else min(activeNums[activeMid], passiveNums[passiveMid]))
    return float(minRight) if odd else ((minRight + maxLeft) / 2)

print(findMedianSortedArrays([1,3], [2]))

