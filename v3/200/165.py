#!/usr/bin/python3

def compareVersion(version1, version2):
    v1Parts = version1.split('.')
    v2Parts = version2.split('.')
    
    i = 0
    while i < len(v1Parts) and i < len(v2Parts):
        v1Part = v1Parts[i]
        v2Part = v2Parts[i]
        if int(v1Part) < int(v2Part):
            return -1
        elif int(v1Part) > int(v2Part):
            return 1
        i += 1
    
    while i < len(v1Parts):
        if int(v1Parts[i]) != 0:
            return 1
        i += 1
    while i < len(v2Parts):
        if int(v2Parts[i]) != 0:
            return -1
        i += 1
    return 0
