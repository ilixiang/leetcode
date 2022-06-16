#!/usr/bin/python3

def countAndSay(n):
    if n == 1:
        return '1'
    
    s = countAndSay(n - 1)
    num = s[0]
    count = 0
    result = ''
    for c in s:
        if c != num:
            result = result + str(count) + num
            count = 1
            num = c
        else:
            count = count + 1
    result = result + str(count) + num
    return result
 

print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
