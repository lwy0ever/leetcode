class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 前缀和+滑动窗口
        # 二分法的复杂度大约N + NlogN
        # 滑动窗口的复杂度大约N
        n = len(fruits)
        preSum = [(0,0)]
        startInd = -1
        for p,a in fruits:
            if p >= startPos and startInd == -1:
                preSum.append((startPos,preSum[-1][1]))
                startInd = len(preSum) - 1
            preSum.append((p,preSum[-1][1] + a))
        if startInd == -1:
            preSum.append((startPos,preSum[-1][1]))
            startInd = len(preSum) - 1
        #print(preSum)
        ans = 0
        l = 1
        r = startInd
        # 保证l <= startPos <= r
        # 有2种走法:
        # 1,左-右,步数 = startPos - l + r - l
        # 2,右-左,步数 = r - startPos + r - l
        while l <= startInd and r < len(preSum):
            #print(f'out:{l},{r}')
            while r < len(preSum) and ((preSum[startInd][0] - preSum[l][0] + preSum[r][0] - preSum[l][0]) <= k or (preSum[r][0] - preSum[startInd][0] + preSum[r][0] - preSum[l][0]) <= k):
                #print(f'in:{l},{r}')
                ans = max(ans,preSum[r][1] - preSum[l - 1][1])
                r += 1
            l += 1
            if l > r:
                r = l
        return ans