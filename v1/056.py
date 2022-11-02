#!/usr/bin/python3

def merge(intervals):
    if len(intervals) == 0:
        return []
    intervals.sort(key = lambda i: i[0])
    mergedInterval = intervals[0]
    result = []
    for interval in intervals:
        if mergedInterval[1] >= interval[0]:
            mergedInterval[1] = max(mergedInterval[1], interval[1])
        else:
            result.append(mergedInterval)
            mergedInterval = interval
    result.append(mergedInterval)
    return result

print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))

