#!/usr/bin/python3

def candy(ratings):
    m = len(ratings)
    if m == 1:
        return 1

    candies = [1] * m
    slopes = [0] * m
    for i in range(1, m):
        slopes[i] = ratings[i] - ratings[i - 1]
    
    i = 0
    top = 0
    bottom = 0
    while i < m:
        while i < m and slopes[i] <= 0:
            i += 1
        bottom = i - 1
        minCandy = 1
        for k in range(bottom, top - 1, -1):
            candies[k] = max(candies[k], minCandy)
            if slopes[k] == 0:
                minCandy = 1
            else:
                minCandy += 1

        while i < m and slopes[i] > 0:
            i += 1
        top = i - 1
        minCandy = 1
        for k in range(bottom, top + 1):
            candies[k] = max(candies[k], minCandy)
            minCandy += 1
        
    print(candies)
    return sum(candies)

