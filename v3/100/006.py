#!/usr/bin/python3

def convert(s, numRows):
    if numRows == 1:
        return s

    n = 2 * numRows - 2
    rev = [None for i in range(len(s))]
    count = len(s) // n + (0 if len(s) % n == 0 else 1)

    cur = 0
    for i in range(numRows):
        for j in range(count):
            first, second = j * n + i, (j + 1) * n - i
            if first >= 0 and first < len(s):
                rev[cur] = s[first]
                cur += 1
            if i > 0 and i < numRows - 1 and second >= 0 and second < len(s):
                rev[cur] = s[second]
                cur += 1
    return ''.join(rev)

if __name__ == '__main__':
    assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
