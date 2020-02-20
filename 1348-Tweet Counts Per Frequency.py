class TweetCounts:

    def __init__(self):
        self.u = collections.defaultdict(list)
        self.m = {'minute':60,'hour':3600,'day':3600 * 24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.u[tweetName],time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.m[freq]
        ans = []
        start = startTime
        pos = bisect.bisect_left(self.u[tweetName],start)
        end = start
        while end <= endTime:
            end = min(end + delta,endTime + 1)
            newPos = bisect.bisect_left(self.u[tweetName],end)
            ans.append(newPos - pos)
            pos = newPos
        return ans
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)