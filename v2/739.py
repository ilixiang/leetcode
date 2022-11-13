#!/usr/bin/python3

def dailyTemperatures(temperatures):
    stack = []
    rev = [0] * len(temperatures)
    for i in range(0, len(temperatures)):
        temperature = temperatures[i]
        while len(stack) != 0 and temperatures[stack[-1]] < temperature:
            prevLowerTemperatureDay = stack.pop()
            rev[prevLowerTemperatureDay] = i - prevLowerTemperatureDay
        stack.append(i)
    return rev
