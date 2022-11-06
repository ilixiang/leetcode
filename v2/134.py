#!/usr/bin/python3

def canCompleteCircuit(gas, cost):
    m = len(gas)
    remain = 0
    minRemain = 0
    minRemainIndex = -1
    for i in range(0, m):
        remain += gas[i] - cost[i]
        if minRemain > remain:
            minRemainIndex = i
            minRemain = remain
    
    if remain < 0:
        return -1
    return (minRemainIndex + 1) % m
