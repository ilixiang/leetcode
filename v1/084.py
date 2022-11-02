#!/usr/bin/python3

def largestRectangleArea(heights):
    length = len(heights)
    leftStack = []
    rightStack = []
    left = [None] * len(heights)
    right = [None] * len(heights)
    result = 0
    for index in range(0, length):
        while len(leftStack) != 0 and (heights[leftStack[-1]] >= heights[index]):
            leftStack.pop()
        left[index] = 0 if len(leftStack) == 0 else (leftStack[-1] + 1)
        leftStack.append(index)
        if right[index] != None:
            result = max(result, heights[index] * (right[index] - left[index] + 1))

        reverseIndex = length - index - 1
        while len(rightStack) != 0 and (heights[rightStack[-1]] >= heights[reverseIndex]):
            rightStack.pop()
        right[reverseIndex] = (length - 1) if len(rightStack) == 0 else (rightStack[-1] - 1)
        rightStack.append(reverseIndex)
        if left[reverseIndex] != None:
            result = max(result, heights[reverseIndex] * (right[reverseIndex] - left[reverseIndex] + 1))
    return result

print(largestRectangleArea([2, 1, 5, 6, 2, 3]))

