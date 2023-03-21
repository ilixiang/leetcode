def partition(s):
    if len(s) == 0:
        return []

    palindromeCache = [[None for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        palindromeCache[i][i] = True
    def isPalindrome(i, j):
        if i > j:
            return True
        if palindromeCache[i][j] != None:
            return palindromeCache[i][j]
        palindromeCache[i][j] = s[i] == s[j] and isPalindrome(i + 1, j - 1)
        return palindromeCache[i][j]
    
    partitionCache = [None for i in range(len(s) + 1)]
    partitionCache[len(s)] = [[]]
    def recursive(start):
        if partitionCache[start] != None:
            return partitionCache[start]

        tmp = []
        for end in range(start, len(s)):
            if isPalindrome(start, end):
                nextPartitions = recursive(end + 1)
                for nextPartition in nextPartitions:
                    tmp.append([s[start:end + 1]] + nextPartition)
        partitionCache[start] = tmp
        return tmp
    return recursive(0)
