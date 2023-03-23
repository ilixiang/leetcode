#!/usr/bin/python3

def longestPalindrome(s):
    if len(s) == 0:
        return ''

    ps = '.' + '.'.join(s) + '.'
    length = len(ps)

    rs = [0 for i in range(len(ps))]
    rev = 0
    center = radius = l = r = 0
    for i in range(len(ps)):
        if i < center + radius:
            j = 2 * center - i
            if j - rs[j] != center - radius:
                rs[i] = rs[j]
                continue
            else:
                l, r = i - rs[j] - 1, i + rs[j] + 1
        else:
            l, r = i - 1, i + 1

        while l >= 0 and r < length and ps[l] == ps[r]:
            l -= 1
            r += 1
        rs[i] = r - i - 1
        if r - i - 1 > radius:
            center = i
            radius = r - i - 1
        
        if radius > rs[rev]:
            rev = center
        
    return s[(rev - rs[rev]) // 2: (rev + rs[rev] + 1) // 2]

if __name__ == '__main__':
    assert longestPalindrome('abc') == 'a'
    assert longestPalindrome('bbc') == 'bb'
    assert longestPalindrome('cbc') == 'cbc'
