#!/usr/bin/python3

def canCompleteCircuit(gas, cost):
    minRemainGasIndex = 0
    minRemainGas = remainGas = gas[0] - cost[0]
    for i in range(1, len(gas)):
        remainGas = remainGas + gas[i] - cost[i]
        if minRemainGas > remainGas:
            minRemainGas = remainGas
            minRemainGasIndex = i
    if remainGas < 0:
        return -1
    return (minRemainGasIndex + 1) % len(gas)
