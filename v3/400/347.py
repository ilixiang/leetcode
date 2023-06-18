#!/usr/bin/python3

import random


def topKFrequent(nums, k):
    frequentMap = {}
    for num in nums:
        frequentMap[num] = frequentMap.get(num, 0) + 1

    frequents = list(map(lambda k: (k, frequentMap[k]), frequentMap))
    m = len(frequents)

    def partition(left, right):
        pivotIdx = random.randint(left, right)
        frequents[pivotIdx], frequents[right] = frequents[right], frequents[pivotIdx]
        pivot = frequents[right][1]
        delimiter = left
        for i in range(left, right):
            if frequents[i][1] <= pivot:
                frequents[i], frequents[delimiter] = frequents[delimiter], frequents[i]
                delimiter += 1
        frequents[delimiter], frequents[right] = frequents[right], frequents[delimiter]
        return delimiter

    left, right = 0, m - 1
    delimiter = partition(left, right)
    while delimiter != m - k:
        if delimiter < m - k:
            left = delimiter + 1
        else:
            right = delimiter - 1
        delimiter = partition(left, right)
    return list(map(lambda a: a[0], frequents[delimiter:]))
