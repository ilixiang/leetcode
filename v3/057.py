#!/usr/bin/python3

def insert(intervals, newInterval):
    rev = []
    i = 0
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        rev.append(intervals[i])
        i += 1
    while i < len(intervals) and (intervals[i][0] <= newInterval[1] and intervals[i][1] >= newInterval[0]):
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    rev.append(newInterval)
    while i < len(intervals):
        rev.append(intervals[i])
        i += 1
    return rev
