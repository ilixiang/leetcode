#!/usr/bin/python3

class Comparator(str):
    def __lt__(s1, s2):
        return (s1 + s2) > (s2 + s1)

def largestNumber(nums):
    return ''.join(sorted(map(lambda n: str(n), nums), key = Comparator))

print(largestNumber([10, 2]))

