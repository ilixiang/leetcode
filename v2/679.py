#!/usr/bin/python3

def judgePoint24(cards):
    def generatePosibleResult(a, b):
        rev = [a + b, a - b, b - a, a * b]
        if a != 0:
            rev.append(b / a)
        
        if b != 0:
            rev.append(a / b)
        return rev
    
    def judgeRecursive(cards):
        if len(cards) == 1:
            return abs(cards[0] - 24.0) < 0.01
        
        for i in range(0, len(cards)):
            for j in range(i + 1, len(cards)):
                nextCards = [num for k, num in enumerate(cards) if (i != k and j != k)]
                for res in generatePosibleResult(cards[i], cards[j]):
                    nextCards.append(res)
                    if judgeRecursive(nextCards):
                        return True
                    nextCards.pop()
        return False
    
    return judgeRecursive(cards)
