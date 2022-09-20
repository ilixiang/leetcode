#!/usr/bin/python3

def canCompleteCircuit(gas, cost):
    remain = 0
    minRemainIndex = -1
    minRemain = 0
    for i in range(0, len(gas)):
        remain += gas[i] - cost[i]
        if remain < minRemain:
            minRemainIndex = i
            minRemain = remain
    if remain < 0:
        return -1
    return (minRemainIndex + 1) % len(gas)

print(canCompleteCircuit([5,8,2,8], [5,6,6,6]))

