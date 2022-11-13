#!/usr/bin/python3

def openLock(deadends, target):
    targetNum = int(target)
    visited = set(map(lambda x: int(x), deadends))
    if 0 in visited:
        return -1

    steps = [1, 10, 100, 1000]
    queue = [0]
    visited.add(0)
    rev = 0
    while len(queue) != 0:
        size = len(queue)
        while size > 0:
            num = queue.pop(0)
            if num == targetNum:
                return rev
            for step in steps:
                nextNum = num
                if (num % (step * 10)) // step == 9:
                    nextNum = num - 9 * step
                else:
                    nextNum = num + step
                if nextNum <= 9999 and not nextNum in visited:
                    queue.append(nextNum)
                    visited.add(nextNum)
            for step in steps:
                nextNum = num
                if (num % (step * 10)) // step == 0:
                    nextNum = num + 9 * step
                else:
                    nextNum = num - step
                if nextNum <= 9999 and not nextNum in visited:
                    queue.append(nextNum)
                    visited.add(nextNum)
            size -= 1
        rev += 1
    return -1
