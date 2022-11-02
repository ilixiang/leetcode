#!/usr/bin/python3

def romanToInt(s):
    mappings = {\
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,\
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,\
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,\
        'M': 1000\
    }

    i = 0
    length = len(s)
    res = 0
    while i < length:
        if i + 1 < length and s[i: i + 2] in mappings:
            res += mappings[s[i: i + 2]]
            i += 2
        else:
            res += mappings[s[i]]
            i += 1
    return res
