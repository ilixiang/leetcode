#!/usr/bin/python3

def hIndex(citations):
    MAX_CITATION = 1000
    counts = [0] * (MAX_CITATION + 1)
    for citation in citations:
        counts[citation] += 1
    
    i = 0
    for citation in range(0, MAX_CITATION + 1):
        count = counts[citation]
        while count != 0:
            citations[i] = citation
            i += 1

    rev = i = 0
    while i < len(citations) and citations[i] <= len(citations) - i:
        rev = citations[i]
        i += 1
    if i < len(citations):
        return max(len(citations) - i, rev)
    return rev
