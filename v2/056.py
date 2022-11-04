#!/usr/bin/python3

def merge(intervals):
    if len(intervals) == 1:
        return intervals
    intervals.sort(key = lambda e: e[0])
    mergingInterval = list(intervals[0])
    res = []
    for interval in intervals:
        if mergingInterval[1] >= interval[0]:
            mergingInterval[1] = max(mergingInterval[1], interval[1])
        else:
            res.append(mergingInterval)
            mergingInterval = list(interval)
    res.append(mergingInterval)
    return res

