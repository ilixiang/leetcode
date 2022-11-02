#!/usr/bin/python3

def candy(ratings):
    bottoms = []
    previousSlope = -1 
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            slop = 1
        elif ratings[i] == ratings[i - 1]:
            slop = 0
        else:
            slop = -1
        if previousSlope < slop:
            bottoms.append(i - 1)
        previousSlope = slop
    if previousSlope == -1:
        bottoms.append(len(ratings) - 1)
    print(bottoms)

    candies = [0] * len(ratings)
    for bottom in bottoms:
        candies[bottom] = 1
        i = bottom - 1
        while i >= 0 and ratings[i] >= ratings[i + 1]:
            candies[i] = max(candies[i], (candies[i + 1] + 1) if ratings[i] > ratings[i + 1] else 1)
            i -= 1
        i = bottom + 1
        while i < len(ratings) and ratings[i] >= ratings[i - 1]:
            candies[i] = max(candies[i], (candies[i - 1] + 1) if ratings[i] > ratings[i - 1] else 1)
            i += 1
    print(candies)
    return sum(candies)

print(candy([1,0,2]))
print(candy([1,2,2]))
print(candy([1,3,2,2,1]))
print(candy([29,51,87,87,72,12]))
            
