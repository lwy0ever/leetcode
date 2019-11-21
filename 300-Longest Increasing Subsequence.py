class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 时间复杂度O(NlogN)
        # 维护一个递增序列res
        # 如果nums的元素应该插入res的最右侧，则res.append()
        # 如果nums的元素应该插入res的其它位置i，则替换其右侧的元素(说明可能存在一个新的res[:i + 1],长度为i,但是末尾元素要比原来的小,这样形成更长res的可能性最大)
        # 最终res的长度,就是答案(但是res本身并不一定是Longest Increasing Subsequence)
        res = []
        for a in nums:
            pos = bisect.bisect_left(res,a)
            if pos == len(res):
                res.append(a)
            else:
                res[pos] = a
        return len(res)
        '''
        # 时间复杂度O(N^2)
        n = len(nums)
        if n == 0:
            return 0
        # dp[i]表示nums[:i + 1]的最长递增序列
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)
        '''
