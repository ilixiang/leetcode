#!/usr/bin/python3

import heapq

def findOrder(numCourses, prerequisites):
    graph = [[] for i in range(0, numCourses)]
    indegrees = [0] * numCourses
    for prerequisite in prerequisites:
        graph[prerequisite[1]].append(prerequisite[0])
        indegrees[prerequisite[0]] += 1
    
    queue = []
    for courseNo in range(0, numCourses):
        if indegrees[courseNo] == 0:
            queue.append(courseNo)
    
    rev = []
    while len(queue) != 0:
        courseNo = queue.pop()
        rev.append(courseNo)
        for postCourseNo in graph[courseNo]:
            indegrees[postCourseNo] -= 1
            if indegrees[postCourseNo] == 0:
                queue.append(postCourseNo)

    if len(rev) != numCourses:
        return []
    return rev

def verifyAnswer(answer, prerequisites, numCourses):
    for courseNo in answer:
        for prerequisite in prerequisites:
            assert prerequisite[0] != courseNo
        prerequisites = [p for p in prerequisites if p[1] != courseNo]
    assert len(prerequisites) == 0