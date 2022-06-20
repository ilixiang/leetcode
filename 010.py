#!/usr/bin/python3

epsilon = lambda : True

class StateNode:
    def __init__(self, state):
        self.state = state
        self.edges = []

class TransferGraph:
    def __init__(self, start, end, matcher):
        self.start = start
        self.end = end
        start.edges.append((matcher, end))

    def addSeries(self, graph):
        self.end.edges.append((epsilon, graph.start))
        self.end = graph.end

    def isMatch(self, s):
        return self.match(s, 0, self.start)
    
    def match(self, s, index, node):
        if node == self.end and index == len(s):
            return True
        for i in range(0, len(node.edges)):
            edge = node.edges[i]
        # for edge in node.edges:
            if edge[0] == epsilon:
                if self.match(s, index, edge[1]):
                    return True
            else:
                if index < len(s) and edge[0](s[index]) and self.match(s, index + 1, edge[1]):
                    return True
        return False

def isMatchRegex(s, p):
    state = 0
    graph = TransferGraph(StateNode(state + 1), StateNode(state + 2), epsilon)
    state = state + 2
    index = 0
    while index < len(p):
        c = p[index]
        if c == '.':
            nextGraph = TransferGraph(StateNode(state + 1), StateNode(state + 2), lambda x: True)
            state = state + 2
            index = index + 1
            if index < len(p) and p[index] == '*':
                newEnd = StateNode(state + 1)
                state = state + 1
                nextGraph.end.edges.append((epsilon, nextGraph.start))
                nextGraph.start.edges.append((epsilon, newEnd))
                nextGraph.end = newEnd
                index = index + 1
            graph.addSeries(nextGraph)
        else:
            nextGraph = TransferGraph(StateNode(state + 1), StateNode(state + 2), lambda left, right = c: left == right)
            state = state + 2
            index = index + 1
            if index < len(p) and p[index] == '*':
                newEnd = StateNode(state + 1)
                state = state + 1
                nextGraph.end.edges.append((epsilon, nextGraph.start))
                nextGraph.start.edges.append((epsilon, newEnd))
                nextGraph.end = newEnd
                index = index + 1
            graph.addSeries(nextGraph)

    return graph.isMatch(s)

def isMatch(s, p):
    dp = []
    for i in range(0, len(p)):
        dp.append([None] * (len(s) + 1))
    dp.append([False] * (len(s) + 1))
    dp[len(p)][len(s)] = True
    return match(s, p, 0, 0, dp)

def match(s, p, sIndex, pIndex, dp):
    if dp[pIndex][sIndex] != None:
        return dp[pIndex][sIndex]
    if pIndex + 1 < len(p) and p[pIndex + 1] == '*':
        if sIndex == len(s) or (s[sIndex] != p[pIndex] and p[pIndex] != '.'):
            dp[pIndex][sIndex] = match(s, p, sIndex, pIndex + 2, dp)
        else:
            dp[pIndex][sIndex] = match(s, p, sIndex, pIndex + 2, dp) or match(s, p, sIndex + 1, pIndex, dp) or match(s, p, sIndex + 1, pIndex + 2, dp)
    else:
        if sIndex == len(s):
            dp[pIndex][sIndex] = False
        else:
            dp[pIndex][sIndex] = (p[pIndex] == s[sIndex] or p[pIndex] == '.') and match(s, p, sIndex + 1, pIndex + 1, dp)
    return dp[pIndex][sIndex]

print(isMatch('aa', 'a'))
print(isMatch('aa', 'a*'))
print(isMatch('ab', '.*'))
print(isMatch('aab', 'c*a*b'))
print(isMatch('bbbba', '.*a*a'))
print(isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'))
