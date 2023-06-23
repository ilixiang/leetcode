#!/usr/bin/python3

import heapq


class Twitter:
    def __init__(self):
        self.order = 0
        self.postMap = {}
        self.followMap = {}

    def postTweet(self, userId, tweetId):
        posts = self.postMap.get(userId, None)
        if posts == None:
            self.postMap[userId] = posts = []
        posts.append((self.order, tweetId))
        self.order += 1
        if len(posts) > 10:
            posts.pop(0)

    def getNewsFeed(self, userId):
        selfPosts = self.postMap.get(userId, [])
        follees = self.followMap.get(userId, [])
        tmp = []
        for post in selfPosts:
            heapq.heappush(tmp, post)
            if len(tmp) > 10:
                heapq.heappop(tmp)
        for follee in follees:
            for post in self.postMap.get(follee, []):
                heapq.heappush(tmp, post)
                if len(tmp) > 10:
                    heapq.heappop(tmp)
        rev = []
        while len(tmp) > 0:
            rev.append(heapq.heappop(tmp)[1])
        return reversed(rev)

    def follow(self, followerId, followeeId):
        followees = self.followMap.get(followerId, None)
        if followees == None:
            self.followMap[followerId] = followees = set()
        followees.add(followeeId)

    def unfollow(self, followerId, followeeId):
        followees = self.followMap.get(followerId, None)
        if followees == None:
            return
        followees.remove(followeeId)
