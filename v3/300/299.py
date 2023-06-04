#!/usr/bin/python3

def getHint(secret, guess):
    m = len(secret)
    secretMap = [0] * 10
    guessMap = [0] * 10
    bulls = 0
    for i in range(m):
        secretDigit = int(secret[i])
        guessDigit = int(guess[i])
        if secretDigit == guessDigit:
            bulls += 1
        else:
            secretMap[secretDigit] += 1
            guessMap[guessDigit] += 1
    cows = 0
    for i in range(10):
        cows += min(secretMap[i], guessMap[i])
    return str(bulls) + 'A' + str(cows) + 'B'
