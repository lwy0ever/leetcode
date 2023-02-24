class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 贪心
        rightMax = list(range(n + 1))   # rightMax[i]表示以i为起点,最远可达的位置
        for i,r in enumerate(ranges):
            s = max(0,i - r)
            e = min(n,i + r)
            rightMax[s] = max(rightMax[s],e)
        ans = 0
        right = 0   # 表示最远可达区域
        pre = 0 # 上一个被使用的子区间的结束位置
        for i in range(n):
            right = max(right,rightMax[i])
            # 水龙头0...i只能浇到i,无法和下一个i + 1连起来
            # 也正因此,只需要检查到位置n - 1,而不需要检查n
            if i == right:
                return -1
            if i == pre:
                pre = right
                ans += 1
        return ans

        # dp
        area = []
        for i,r in enumerate(ranges):
            area.append([max(0,i - r),min(n,i + r)])
        area.sort()

        dp = [float('inf')] * (n + 1)   # dp[i]表示灌溉到i,最少的次数
        dp[0] = 0
        for s,e in area:
            if dp[s] > n:
                return -1
            for j in range(s,e + 1):
                dp[j] = min(dp[j],dp[s] + 1)
        return dp[n]

        # 类似贪心
        area = []   # area[i] = (from,to)表示水龙头i的覆盖范围是[from,to]
        for i in range(n + 1):
            area.append([i - ranges[i],i + ranges[i]])
        area.sort(key = lambda x:(x[0],-x[1]))
        #print(area)
        ans = 0
        _max = -1   # 灌溉的最远范围
        i = 0   # 灌溉到的水龙头位置
        cur = 0 # area的指针
        while i <= n:
            #print('i:',i)
            #toadd = False
            while cur <= n and i >= area[cur][0]:   # 找到所有能覆盖到i的范围的水龙头
                if area[cur][1] > _max:
                    _max = area[cur][1] # 获取最远灌溉范围
                #print(cur,i,area[cur],_max,ans)
                cur += 1
            ans += 1    # 需要数量+1
            if _max >= n:   # 已经全覆盖,返回结果
                return ans
            if _max < i + 1:    # 没有找到能覆盖到i + 1的水龙头,说明中断了
                return -1
            i = _max    # 更新最远范围
        return ans