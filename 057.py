#!/usr/bin/python3

def insert(intervals, newInterval):
    index = 0
    result = []
    while index < len(intervals):
        interval = intervals[index]
        if interval[0] < newInterval[0]:
            if interval[1] < newInterval[0]:
                result.append(interval)
                index = index + 1
            else:
                newInterval = [interval[0], max(interval[1], newInterval[1])]
                index = index + 1
        else:
            if interval[0] > newInterval[1]:
                break
            else:
                newInterval = [newInterval[0], max(interval[1], newInterval[1])]
                index = index + 1
    result.append(newInterval)
    while index < len(intervals):
        result.append(intervals[index])
        index = index + 1
    return result

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(insert([],[4,8]))

