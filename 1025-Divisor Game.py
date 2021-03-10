class Solution:
    def divisorGame(self, N: int) -> bool:
        # 找规律,奇数输,偶数赢
        return N & 1 == 0
        
        # 递推
        '''
        dp = [False]    # dp[i] 表示N = i + 1时的胜负情况
        for i in range(2,N + 1):
            for x in range(1,i):
                if i % x == 0 and dp[i - x - 1] == False:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        #print(dp)
        return dp[-1]
        '''