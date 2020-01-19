class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.f = collections.defaultdict(set)  # f[followerId] = {followeeId1,followeeId2...}
        self.time = 0
        self.tweet = collections.defaultdict(list)  # tweet[userId] = [(tweetId1,time1),(tweetId2,time2)...]


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        #print('postTweet',userId,tweetId)
        self.tweet[userId].append((tweetId,self.time))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        #print('getNewsFeed',userId)
        userCur = dict()
        time = []   # 时间顺序
        orderedUser = [] # 按照时间顺序存储userId
        #print(self.f[userId] | {userId})
        for u in self.f[userId] | {userId}:
            if len(self.tweet[u]) > 0:
                userCur[u] = -1
                loc = bisect.bisect(time,self.tweet[u][-1][1])
                time.insert(loc,self.tweet[u][-1][1])
                orderedUser.insert(loc,u)
        cnt = 0
        ans = []
        while cnt < 10 and orderedUser:
            time.pop()
            lastUser = orderedUser.pop()
            ans.append(self.tweet[lastUser][userCur[lastUser]][0])
            userCur[lastUser] -= 1
            if -userCur[lastUser] <= len(self.tweet[lastUser]):
                loc = bisect.bisect(time,self.tweet[lastUser][userCur[lastUser]][1])
                time.insert(loc,self.tweet[lastUser][userCur[lastUser]][1])
                orderedUser.insert(loc,lastUser)
            cnt += 1
            #print(time)
            #print(orderedUser)
            #print(userCur)
            #print(lastUser)
            #print(ans)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.f[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.f[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)