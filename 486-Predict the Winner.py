class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp内存优化
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = nums[i]
        for l in range(1,n):
            for i in range(n - l):
                j = i + l
                dp[i] = max(nums[i] - dp[i + 1],nums[j] - dp[i])
        return dp[0] >= 0

        '''
        # dp
        # dp[i][j]表示在nums[i:j + 1]范围内,先手一方可以比后手一方多的分数
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for l in range(1,n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = max(nums[i] - dp[i + 1][j],nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
        '''

        '''
        # O(2 ** N)
        # 当前玩家得分s1,对手得分s2
        # 当前考虑范围nums[left:right]
        # isFirst表示s1是否是玩家1
        # 可以获胜的情况下返回True,否则返回Fasle
        def c(s1,s2,left,right,isFirst):
            if left == right:
                if isFirst:
                    return s1 >= s2
                else:
                    return s1 > s2
            if not c(s2,s1 + nums[left],left + 1,right,not isFirst) or not c(s2,s1 + nums[right - 1],left,right - 1,not isFirst):
                return True
            return False
        
        return c(0,0,0,len(nums),True)
        '''