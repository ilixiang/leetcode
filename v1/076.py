#!/usr/bin/python3

def minWindow(s, t):
    if s == '' or t == '':
        return ''

    # initialize tMap
    tMap = {}
    for i in range(0, len(t)):
        c = t[i]
        if not c in tMap:
            tMap[c] = (1, [])
        else:
            (tCount, tIndices) = tMap[c]
            tMap[c] = (tCount + 1, tIndices)
    print(tMap)

    remainCharCount = len(tMap)
    rev = None
    left = 0
    right = 0
    while left < len(s) and right < len(s):
        while right < len(s):
            c = s[right]
            if not c in tMap:
                right += 1
                continue
            (cCount, cIndices) = tMap[c]
            cIndices.append(right)
            if len(cIndices) == cCount:
                remainCharCount -= 1
            if remainCharCount == 0:
                right += 1
                break
            right += 1

        while left < right:
            c = s[left]
            if not c in tMap:
                left += 1
                continue
            (cCount, cIndices) = tMap[c]
            if cCount < len(cIndices):
                cIndices.pop(0)
                left += 1
            else:
                rev = s[left:right] if remainCharCount == 0 and (rev == None or len(rev) > right - left) else rev
                break

    return '' if rev == None else rev

print(minWindow('abcabdebac', 'cda'))

