#!/usr/bin/python3

def removeInvalidParentheses(s):
    def isValid(s):
        left = right = 0
        for c in s:
            if left < right:
                return False
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
        return left == right
    
    maxLen = -1
    res = set()
    queue = [(s, 0)]
    while len(queue) != 0:
        (t, pos) = queue.pop(0)
        if maxLen != -1 and len(t) < maxLen:
            break
        if isValid(t):
            res.add(t)
            maxLen = len(t)
        i = pos
        for i in range(pos, len(t)):
            if (t[i] == '(' or t[i] == ')') and (i == pos or t[i] != t[i - 1]):
                queue.append((t[:i] + t[i+1:], i))
    return list(res)

if __name__ == '__main__':
    print(removeInvalidParentheses('()())()'))
    print(removeInvalidParentheses('(a)())()'))
    print(removeInvalidParentheses(')('))
