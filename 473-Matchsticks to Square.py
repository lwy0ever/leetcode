class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # dp
        # dp[mask]表示使用状态为mask时,未放满的边的长度(会经历4次放满的过程)
        n = len(matchsticks)
        if n < 4:
            return False
        s = sum(matchsticks)
        if s & 3 != 0:
            return False
        length = s // 4

        dp = [-1] * (1 << n)
        dp[0] = 0
        for mask in range(1,1 << n):
            for i,v in enumerate(matchsticks):
                if mask & (1 << i): # 当前状态mask使用过第i个值,可以检查前一个状态
                    preMask = mask & ~(1 << i)
                    if dp[preMask] >= 0 and dp[preMask] + v <= length:
                        dp[mask] = (dp[preMask] + v) % length   # 如果==length,则说明一条边放好了,可以归零
                        break
        return dp[-1] == 0


        # 会超时
        '''
        n = len(matchsticks)
        if n < 4:
            return False
        s = sum(matchsticks)
        if s & 3 != 0:
            return False
        length = s // 4
        matchsticks.sort(reverse = True)
        if matchsticks[0] > length:
            return False

        # need:需要尝试的边数
        # added:这个边已经达到的长度
        # mask:使用记录
        def helper(need,added,mask):
            if need == 0:
                return True
            if added == length:
                return helper(need - 1,0,mask)
            if added == 0:
                for i in range(n):
                    if (1 << i) & mask == 0:
                        return helper(need,matchsticks[i],(1 << i) | mask)
                return False
            for i in range(n):
                if (1 << i) & mask == 0 and added + matchsticks[i] <= length:
                    if helper(need,added + matchsticks[i],(1 << i) | mask):
                        return True
            return False

        return helper(3,0,0)
        '''