#!/usr/bin/python3

def removeDuplicateLetters(s):
        lastIdxList = [-1] * 26
        for i in range(len(s)):
            lastIdxList[ord(s[i]) - 97] = i
        
        visited = [False] * 26
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            cIdx = ord(c) - 97
            if not visited[cIdx] and len(stack) != 0 and c < stack[-1] and i < lastIdxList[ord(stack[-1]) - 97]:
                visited[ord(stack.pop()) - 97] = False
                continue
            if not visited[cIdx]:
                stack.append(c)
                visited[cIdx] = True
            i += 1
        return ''.join(stack)
