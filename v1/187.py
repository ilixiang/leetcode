#!/usr/bin/python3

def findRepeatedDnaSequences(s):
    length = len(s)
    if length < 10:
        return []
    m = {}
    for index in range(0, length - 9):
        seq = s[index:index + 10] 
        if seq not in m:
            m[seq] = 0
        m[seq] = m[seq] + 1

    result = []
    for seq in m.keys():
        if m[seq] > 1:
            result.append(seq)
    return result

print(findRepeatedDnaSequences('AAAAAAAAAAAAA'))


