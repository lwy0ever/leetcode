class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        idxes = collections.defaultdict(list)
        for i, v in enumerate(arr):
            idxes[v].append(i)
        
        from functools import lru_cache
        @lru_cache(None)
        def dfs(s, e):
            if s > e: return 0
            if s == e: return 1
            if s + 1 == e: return 1 if arr[s] == arr[e] else 2
            res = 1 + dfs(s + 1, e)
            first = arr[s]
            cdd = idxes[first]
            ind1 = bisect.bisect_left(cdd, s + 1)
            ind2 = bisect.bisect_right(cdd, e)
            for k in range(ind1, ind2):
                if s == cdd[k] - 1 or s == cdd[k] - 2:
                    res = min(res, 1 + dfs(cdd[k] + 1, e))
                    continue
                res = min(res, dfs(s + 1, cdd[k] - 1) + dfs(cdd[k] + 1, e))
            return res

        return dfs(0, len(arr) - 1)
        '''
        # dp[i][j]表示删掉arr[i:j + 1]用的最小次数
        n = len(arr)
        #dp = [[n] * n for _ in range(n)]    # 最多需要n次
        dp = [array.array('h',[n] * n) for _ in range(n)]
        # 长度为1
        for i in range(n):
            dp[i][i] = 1
        # 长度为2
        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                dp[i][i + 1] = 1
            else:
                dp[i][i + 1] = 2
        # 观察长度，从3到n
        for length in range(3,n + 1):
            # 起始位置
            for left in range(0,n - length + 1):
                # 结束位置
                right = left + length - 1
                for mid in range(left,right):
                    # 左右分别删除的最优解
                    dp[left][right] = min(dp[left][right],dp[left][mid] + dp[mid + 1][right])
                # 如果arr[left] == arr[right],那么可以在dp[left + 1][right - 1]次内删除
                if arr[left] == arr[right]:
                    dp[left][right] = min(dp[left][right],dp[left + 1][right - 1])
        #print(dp)
        return dp[0][n - 1]
        '''