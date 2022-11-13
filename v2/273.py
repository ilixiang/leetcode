#!/usr/bin/python3

def numberToWords(num):
    lookup = [\
        (10 ** 9, 'Billion'),\
        (10 ** 6, 'Million'),\
        (10 ** 3, 'Thousand'),\
        (10 ** 2, 'Hundred'),\
        (90, 'Ninety'),\
        (80, 'Eighty'),\
        (70, 'Seventy'),\
        (60, 'Sixty'),\
        (50, 'Fifty'),\
        (40, 'Forty'),\
        (30, 'Thirty'),\
        (20, 'Twenty')
    ]
    directMappings = [
        'Zero',\
        'One',\
        'Two',\
        'Three',\
        'Four',\
        'Five',\
        'Six',\
        'Seven',\
        'Eight',\
        'Nine',\
        'Ten',\
        'Eleven',\
        'Twelve',\
        'Thirteen',\
        'Fourteen',\
        'Fifteen',\
        'Sixteen',\
        'Seventeen',\
        'Eighteen',\
        'Nineteen',\
        'Twenty'
    ]

    def recursive(num):
        if num <= 20:
            return directMappings[num]
        tmp = []
        i = 0
        while i < len(lookup) and num > 20:
            (arabic, eng) = lookup[i]
            quotient = num // arabic
            if quotient != 0:
                if arabic >= 100:
                    tmp.append(recursive(quotient))
                tmp.append(eng)
            num %= arabic
            i += 1
        if num != 0:
            tmp.append(directMappings[num])
        return ' '.join(tmp)
    return recursive(num)
