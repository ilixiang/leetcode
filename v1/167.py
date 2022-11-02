#!/usr/bin/python3

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left, right]
        elif s > target:
            right = right - 1
        else:
            left = left + 1
    return [-1, -1]

