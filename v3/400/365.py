#!/usr/bin/python3

def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    if jug1Capacity + jug2Capacity < targetCapacity:
        return False
    queue = [(0, 0)]
    visited = set(queue)
    while len(queue) != 0:
        (j1, j2) = queue.pop(0)
        if (j1 - targetCapacity) % jug2Capacity == 0 or (j2 - targetCapacity) % jug1Capacity == 0:
            return True
        nextStates = [(0, j2), (j1, 0), (j1, jug2Capacity), (jug1Capacity, j2), (j1 + j2, 0), (jug1Capacity, j1 + j2 - jug1Capacity), (0, j2 + j1), (j2 + j1 - jug2Capacity, jug2Capacity)]
        for nextState in nextStates:
            (nextJ1, nextJ2) = nextState
            if nextJ1 >= 0 and nextJ1 <= jug1Capacity and nextJ2 >= 0 and nextJ2 <= jug2Capacity and not (nextJ1, nextJ2) in visited:
                queue.append(nextState)
                visited.add(nextState)
    return False
