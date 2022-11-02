#!/usr/bin/python3

def intToRoman(num):
    mappings = [\
        (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'),\
        (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'),\
        (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'),\
        (1000, 'M')
        ]
    tmp = []
    i = len(mapping) - 1
    while i >= 0 and num != 0:
        mapping = mappings[i]
        tmp.extend([mapping[1]] * (num // mapping[0]))
        num = num % mapping[0]
        i -= 1;
    return ''.join(tmp)

