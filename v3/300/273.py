#!/usr/bin/python3

def numberToWords(num):
    if num == 0:
        return 'Zero'

    ZERO = 'Zero'
    ONE_TO_NINETEEN = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    MULTIPLE_OF_TEN = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    SEPERATIONS = ['', 'Thousand', 'Million', 'Billion']
    def transferUnderThousand(num):
        if num == 0:
            return ZERO
        tmp = []
        hundreds = num // 100
        if hundreds != 0:
            tmp.append(ONE_TO_NINETEEN[hundreds] + ' Hundred')
        underHundred = num % 100
        if underHundred != 0:
            if underHundred in ONE_TO_NINETEEN:
                tmp.append(ONE_TO_NINETEEN[underHundred])
            else:
                tmp.append(MULTIPLE_OF_TEN[underHundred // 10])
                digit = underHundred % 10
                if digit != 0:
                    tmp.append(ONE_TO_NINETEEN[digit])
        return ' '.join(tmp)
    
    rev = ''
    i = 0 
    while num != 0:
        remainder = num % 1000
        if remainder != 0:
            rev = transferUnderThousand(remainder) + ' ' + SEPERATIONS[i] + ' ' + rev
        num //= 1000
        i += 1
    return rev.strip()