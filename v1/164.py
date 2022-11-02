#!/usr/bin/python3

def maximumGap(nums):
    if len(nums) <= 1:
        return 0

    buckets = [None] * 10
    oBuckets = [None] * 10
    sortedNums = []
    for i in range(0, 10):
        buckets[i] = []
        oBuckets[i] = []
    buckets[0] = nums

    for exponent in range(0, 9):
        print(buckets)
        for bucket in buckets:
            for num in bucket:
                oBuckets[(num // (10 ** exponent)) % 10].append(num)
            bucket.clear()
        tmp = buckets
        buckets = oBuckets
        oBuckets = tmp
    for bucket in buckets:
        sortedNums.extend(bucket)
    rev = 0
    for i in range(1, len(sortedNums)):
        rev = max(rev, abs(sortedNums[i] - sortedNums[i - 1]))
    return rev
        
print(maximumGap([3,6,9,1]))
print(maximumGap([10, 13, 5, 2, 9]))

