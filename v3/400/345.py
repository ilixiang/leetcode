def reverseVowels(s):
    vs = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    cs = list(s)
    l, r = 0, len(cs) - 1
    while l < r:
        if not cs[l] in vs:
            l += 1
        elif not cs[r] in vs:
            r -= 1
        else:
            cs[l], cs[r] = cs[r], cs[l]
            l += 1
            r -= 1
    return ''.join(cs)
