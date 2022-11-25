#!/usr/bin/python3

def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    d = [None] * len(envelopes)
    d[0] = envelopes[0][1]
    l = 1
    for i in range(1, len(envelopes)):
        envelope = envelopes[i]
        if envelope[1] > d[l - 1]:
            d[l] = envelope[1]
            l += 1
        else:
            low, high = 0, l - 1
            pos = -1
            while low <= high:
                mid = (low + high) >> 1
                if d[mid] < envelope[1]:
                    pos = mid
                    low = mid + 1
                else:
                    high = mid - 1
            d[pos + 1] = envelope[1]
    return l
