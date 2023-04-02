#!/usr/bin/python3

def findOrder(numCourses, prerequisites):
    degrees = [0] * numCourses
    graph = [[] for i in range(numCourses)]
    for prerequisite in prerequisites:
        graph[prerequisite[1]].append(prerequisite)
        degrees[prerequisite[0]] += 1
    
    queue = list(filter(lambda i: degrees[i] == 0, range(numCourses)))
    i = 0
    rev = [0] * numCourses
    while len(queue) != 0:
        course = queue.pop(0)
        for prerequisite in graph[course]:
            nextCourse = prerequisite[0]
            degrees[nextCourse] -= 1
            if degrees[nextCourse] == 0:
                queue.append(nextCourse)
        rev[i] = course
        i += 1
    return rev if i == numCourses else []

