#!/usr/bin/python3

class Comparator(str):
    def __lt__(s1, s2):
        return (s1 + s2) > (s2 + s1)

def largestNumber(self, nums):
    rev = ''.join(sorted(map(lambda x: str(x), nums), key = Comparator))
    return '0' if rev[0] == '0' else rev