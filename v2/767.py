#!/usr/bin/python3

def reorganizeString(s):
    charCountMap = {}
    for c in s:
        if not c in charCountMap:
            charCountMap[c] = 1
        else:
            charCountMap[c] += 1
    
    size = len(charCountMap)
    heap = []
    for c in charCountMap:
        heap.append((c, charCountMap[c]))
    def heapify(i):
        lastNonLeafIndex = (size - 2) // 2
        while i <= lastNonLeafIndex:
            left = 2 * i + 1
            right = 2 * i + 2
            candidate = left if right >= size or heap[left][1] > heap[right][1] else right
            if heap[candidate][1] <= heap[i][1]:
                break
            heap[candidate], heap[i] = heap[i], heap[candidate]
            i = candidate
    
    i = (size - 2) // 2
    while i >= 0:
        heapify(i)
        i -= 1
    
    rev = [None] * len(s)
    for i in range(0, len(s)):
        print(heap)
        (maxCountChar, charCount) = heap[0]
        if i == 0 or rev[i - 1] != maxCountChar:
            rev[i] = maxCountChar
            heap[0] = (maxCountChar, charCount - 1)
            heapify(0)
        else:
            if len(heap) > 1:
                changedIndex = 1
                (secondMostChar, charCount) = heap[1]
                if len(heap) > 2 and heap[2][1] > charCount:
                    changedIndex = 2
                    (secondMostChar, charCount) = heap[2]
                if charCount == 0:
                    return ''
                rev[i] = secondMostChar
                heap[changedIndex] = (secondMostChar, charCount - 1)
                heapify(changedIndex)
            else:
                return ''
    return ''.join(rev)

