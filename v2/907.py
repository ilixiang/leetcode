#!/usr/bin/python3

def sumSubarrayMins(arr):
    rev = 0
    stack = []
    for i in range(0, len(arr)):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            popedIndex = stack.pop()
            rev = (rev + (popedIndex - (-1 if len(stack) == 0 else stack[-1])) * (i - popedIndex) * arr[popedIndex]) % (10 ** 9 + 7)
        stack.append(i)

    for i in range(0, len(stack)):
        leftPosibility = stack[i] - (-1 if i == 0 else stack[i - 1])
        rightPosibility = len(arr) - stack[i]
        rev = (rev + leftPosibility * rightPosibility * arr[stack[i]]) % (10 ** 9 + 7)
    return rev
