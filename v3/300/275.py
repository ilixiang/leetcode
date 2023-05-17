#!/usr/bin/python3

def hIndex(citations):
    n = len(citations)
    if n == 0:
        return 0
    
    delimiter = -1
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) >> 1
        if citations[mid] <= n - mid:
            delimiter = mid
            left = mid + 1
        else:
            right = mid - 1
    rev = 0
    if delimiter >= 0:
        rev = citations[delimiter]
    return max(rev, n - delimiter - 1)
