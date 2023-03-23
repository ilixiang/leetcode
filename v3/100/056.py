#!/usr/bin/python3

def merge(intervals):
    intervals.sort(key = lambda e: e[0])
    
    rev = []
    tmp = intervals[0]
    for interval in intervals:
        if tmp[1] >= interval[0]:
            tmp[1] = max(tmp[1], interval[1])
        else:
            rev.append(tmp)
            tmp = interval
    rev.append(tmp)
    return rev
