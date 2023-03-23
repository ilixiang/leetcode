#!/usr/bin/python3

def findSubstring(s, words):
    m = {}
    for word in words:
        m[word] = m.get(word, 0) + 1
    
    rev = []
    remain = len(words)
    length = len(words[0])
    for start in range(0, length):
        left = right = start
        while right + length <= len(s):
            word = s[right:right + length]
            need = m.get(word, None)
            if need == 0:
                while s[left:left + length] != word:
                    discardWordNeed = m[s[left:left + length]]
                    m[s[left:left + length]] = discardWordNeed + 1
                    remain += 1
                    left += length
                left += length
            elif need == None:
                while left != right:
                    discardWordNeed = m[s[left:left + length]]
                    m[s[left:left + length]] = discardWordNeed + 1
                    left += length
                left += length
                remain = len(words)
            else:
                m[word] = need - 1
                remain -= 1
                if remain == 0:
                    rev.append(left)
                    m[s[left:left + length]] += 1
                    left += length
                    remain += 1
            right += length

        while left != right:
            m[s[left:left + length]] += 1
            left += length
        remain = len(words)
    return rev


if __name__ == '__main__':
    rev = findSubstring('barfoothefoobarman', ['foo', 'bar'])
    assert len(rev) == 2
    assert 0 in rev and 9 in rev

    rev = findSubstring('wordgoodgoodgoodbestword', ['word','good','best','word'])
    assert len(rev) == 0

    rev = findSubstring('wordgoodgoodgoodbestword', ['word','good','best','good'])
    assert len(rev) == 1
    assert 8 in rev