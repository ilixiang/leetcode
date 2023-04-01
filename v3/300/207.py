#!/usr/bin/python3

def canFinish(numCourses, prerequisites):
    degrees = [0 for i in range(numCourses)]
    graph = [[] for i in range(numCourses)]
    for prerequisite in prerequisites:
        degrees[prerequisite[0]] += 1
        graph[prerequisite[1]].append(prerequisite)
    
    learnedCourseNum = 0
    queue = list(filter(lambda x: degrees[x] == 0, range(numCourses)))
    while len(queue) != 0:
        course = queue.pop(0)
        for prerequisite in graph[course]:
            nextCourse = prerequisite[0]
            degrees[nextCourse] -= 1
            if degrees[nextCourse] == 0:
                queue.append(nextCourse)
        learnedCourseNum += 1
    return learnedCourseNum == numCourses
