class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        # 按照宽度升序,高度倒序
        # 这样宽度不用再考虑,只需要考虑高度
        # 找到高度的最长升序子序列即可
        envelopes.sort(key = lambda x:(x[0],-x[1]))
        
        dp = []
        dp.append(envelopes[0][1])
        ans = 1
        # 转化为 最长严格递增子序列 问题
        for w,h in envelopes[1:]:
            if h > dp[-1]:
                dp.append(h)
                ans += 1
            else:
                loc = bisect.bisect_left(dp,h)
                dp[loc] = h
        return ans