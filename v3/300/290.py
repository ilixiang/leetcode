#!/usr/bin/python3

def wordPattern(pattern, s):
    words = s.split(' ');
    if len(words) != len(pattern):
        return False

    m = len(words)
    map = {}
    rMap = {}
    for i in range(m):
        word = words[i]
        char = pattern[i]

        charMapping = map.get(char, None)
        wordMapping = rMap.get(word, None)
        if charMapping == None and wordMapping == None:
            map[char] = word
            rMap[word] = char
            continue
        if charMapping != word or wordMapping != char:
            return False
    return True
