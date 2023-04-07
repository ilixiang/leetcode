#!/usr/bin/python3

def shortestPalindrome(s):
    ps = '*' + '*'.join(s) + '*'
    radiuses = [0] * len(ps)
    center = 0
    covered = 0
    
    maxBeginPalindromeLength = 3
    cur = 1
    while cur < len(ps):
        if cur > covered:
            left, right = cur - 1, cur + 1
            while left >= 0 and right < len(ps) and ps[left] == ps[right]:
                left -= 1
                right += 1
            center, covered = cur, right - 1
            radiuses[cur] = covered - center
        else:
            symmetryRadius = radiuses[2 * center - cur]
            if cur + symmetryRadius != covered:
                radiuses[cur] = min(symmetryRadius, covered - cur)
            else:
                left, right = 2 * cur - covered - 1, covered + 1
                while left >= 0 and right < len(ps) and ps[left] == ps[right]:
                    left -= 1
                    right += 1
                center, covered = cur, right - 1
                radiuses[cur] = covered - center
        if cur - radiuses[cur] == 0:
            maxBeginPalindromeLength = max(maxBeginPalindromeLength, cur + radiuses[cur] + 1)
        cur += 1

    maxBeginPalindromeLength >>= 1
    return s[-1:maxBeginPalindromeLength - 1:-1] + s

if __name__ == '__main__':
    shortestPalindrome('aacecaaa')
