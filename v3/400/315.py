#!/usr/bin/python3

def countSmallerMergeSort(nums):
    rev = [0] * len(nums)
    def mergeSort(left, right):
        if left == right:
            return []
        if left == right - 1:
            return [left]
        
        mid = (left + right) >> 1
        sortedLeft = mergeSort(left, mid)
        sortedRight = mergeSort(mid, right)
        i = j = 0
        merged = [0] * (right - left)
        smallerCount = 0
        while i < len(sortedLeft) and j < len(sortedRight):
            leftVal = nums[sortedLeft[i]]
            rightVal = nums[sortedRight[j]]
            if leftVal <= rightVal:
                merged[i + j] = sortedLeft[i]
                rev[sortedLeft[i]] += smallerCount
                i += 1
            else:
                merged[i + j] = sortedRight[j]
                smallerCount += 1
                j += 1
        while i < len(sortedLeft):
            merged[i + j] = sortedLeft[i]
            rev[sortedLeft[i]] += smallerCount
            i += 1
        while j < len(sortedRight):
            merged[i + j] = sortedRight[j]
            j += 1
        return merged 
    mergeSort(0, len(nums))
    return rev

def countSmallerBinaryIndexedTree(nums):
    MAX_VAL = max(nums)
    MIN_VAL = min(nums)
    DATA_RANGE_SIZE = MAX_VAL - MIN_VAL + 1
    TREE_SIZE = DATA_RANGE_SIZE + 1

    counts = [0] * (len(nums))
    tree = [0] * TREE_SIZE
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        dataIdx = num - MIN_VAL
        treeIdx = dataIdx + 1
        # query tree
        count = 0
        while dataIdx > 0:
            count += tree[dataIdx]
            dataIdx -= dataIdx & (-dataIdx)
        counts[i] = count

        # update tree
        while treeIdx < TREE_SIZE:
            tree[treeIdx] += 1
            treeIdx += treeIdx & (-treeIdx)
    return counts
