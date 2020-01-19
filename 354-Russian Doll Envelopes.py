class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        # 按照宽度升序,高度倒序
        # 这样宽度不用再考虑,只需要考虑高度
        # 找到高度的最长升序子序列即可
        envelopes.sort(key = lambda x:(x[0],-x[1]))
        
        dp = []
        for w,h in envelopes:
            loc = bisect.bisect_left(dp,h)
            if loc == len(dp):
                dp.append(h)
            else:
                dp[loc] = h
        return len(dp)
        