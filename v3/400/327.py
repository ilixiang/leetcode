#!/usr/bin/python3

def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    prefixes = [0] * (len(nums) + 1)
    s = 0
    for i in range(len(nums)):
        prefixes[i] = s
        s += nums[i]
    prefixes[len(nums)] = s

    def mergeSort(left, right):
        if right <= left + 1:
            return 0

        tmp = [0] * (right - left)
        mid = (left + right) >> 1
        leftRev = mergeSort(left, mid)
        rightRev = mergeSort(mid, right)

        rev = leftRev + rightRev
        a = b = left
        for c in range(mid, right):
            while a < mid and prefixes[a] < prefixes[c] - upper:
                a += 1
            while b < mid and prefixes[b] <= prefixes[c] - lower:
                b += 1
            rev += b - a

        i, j, idx = left, mid, 0
        while i < mid and j < right:
            diff = prefixes[j] - prefixes[i]
            if diff < 0:
                tmp[idx] = prefixes[j]
                j += 1
            else:
                tmp[idx] = prefixes[i]
                i += 1
            idx += 1
        while i < mid:
            tmp[idx] = prefixes[i]
            i += 1
            idx += 1
        for i in range(idx):
            prefixes[left + i] = tmp[i]
        return rev
    return mergeSort(0, len(nums) + 1)

