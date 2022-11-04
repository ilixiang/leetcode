#!/usr/bin/python3

def insert(intervals, newInterval):
    res = []

    i = 0
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    
    mergingInterval = list(newInterval)
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        mergingInterval[0] = min(mergingInterval[0], intervals[i][0])
        mergingInterval[1] = max(mergingInterval[1], intervals[i][1])
        i += 1
    res.append(mergingInterval)

    while i < len(intervals):
        res.append(intervals[i])
        i += 1
    return res

