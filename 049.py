#!/usr/bin/python3

def groupAnagrams(strs):
    if len(strs) == 0:
        return []

    result = []
    m = {}
    for s in strs:
        chars = list(map(lambda i: s[i], range(0, len(s))))
        chars.sort()
        sortedWord = ''.join(chars)
        if sortedWord in m:
            m[sortedWord].append(s)
        else:
            a = [s]
            m[sortedWord] = a
            result.append(a)
    return result

print(groupAnagrams(['eat','tea','tan','ate','nat','bat']))

