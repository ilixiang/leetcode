#!/usr/bin/python3

def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    rev = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
    overlappingWidth = 0
    if ax1 <= bx1 and bx1 < ax2:
        overlappingWidth = min(ax2, bx2) - bx1
    elif bx1 <= ax1 and ax1 < bx2:
        overlappingWidth = min(ax2, bx2) - ax1
    else:
        return rev
    
    overlappingHeight = 0
    if ay1 <= by1 and by1 < ay2:
        overlappingHeight = min(ay2, by2) - by1
    elif by1 <= ay1 and ay1 < by2:
        overlappingHeight = min(ay2, by2) - ay1
    else:
        return rev

    rev -= overlappingWidth * overlappingHeight
    return rev
