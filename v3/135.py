#!/usr/bin/python3

def candy(ratings):
    UP, DOWN = 1, -1
    m = len(ratings)
    candies = [1] * m
    diffs = [0] * m
    for i in range(m - 1):
        diffs[i] = ratings[i + 1] - ratings[i]
    diffs[m - 1] = 0
    l = r = 0
    direction = DOWN if diffs[0] < 0 else UP
    while r < m:
        if direction == UP:
            if diffs[r] < 0:
                direction = DOWN
                curCandy = 1
                for i in range(l, r + 1):
                    candies[i] = max(curCandy, candies[i])
                    curCandy += 1
                    if diffs[i] == 0:
                        curCandy = 1
                l = r
        else:
            if diffs[r] > 0:
                direction = UP
                curCandy = 1
                for i in range(r, l - 1, -1):
                    candies[i] = max(curCandy, candies[i])
                    curCandy += 1
                    if diffs[i - 1] == 0:
                        curCandy = 1
                l = r
        r += 1
    
    if direction == UP:
        curCandy = 1
        for i in range(l, r):
            candies[i] = max(curCandy, candies[i])
            curCandy += 1
            if diffs[i] == 0:
                curCandy = 1
    else:
        curCandy = 1
        for i in range(r - 1, l - 1, -1):
            candies[i] = max(curCandy, candies[i])
            curCandy += 1
            if diffs[i - 1] == 0:
                curCandy = 1
    return sum(candies)
