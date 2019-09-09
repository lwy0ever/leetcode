class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = {} # dp(i,j)表示猜测[i,j]需要的最小金额
        for i in range(1,n + 1):    # 长度为1的区间
            dp[(i,i)] = 0
        for l in range(2,n + 1):    # 长度为l的区间
            for i in range(1,n + 2 - l):    # 猜测的左区间
                j = i + l - 1
                mi = float('inf')   # 猜测区间[i,j]需要的最小金额
                #for guess in range(i,j + 1):
                # 优化，不需要猜测左半区间
                for guess in range((i + j) // 2,j + 1):
                    # 猜测guess的最少花费金额为: max(dp[(i,guess - 1)], dp[(guess + 1,j)]) + guess
                    # 用max的原因是我们要计算最坏反馈情况下的最少花费金额(选了guess之后, 正确数字落在花费更高的那侧)
                    res = guess + max(dp[(i,max(guess - 1,i))], dp[(min(guess + 1,j),j)])
                    mi = min(mi,res)
                dp[(i,j)] = mi
        return dp[(1,n)]        