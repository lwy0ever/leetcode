class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # 记录每个点(包含自身)左侧第一次出现蜡烛的位置
        leftCandlePos = [-1] * n
        pre = -1
        for i in range(n):
            if s[i] == '|':
                pre = i
            leftCandlePos[i] = pre
        #print(leftCandlePos)
        # 记录每个点(包含自身)右侧第一次出现蜡烛的位置
        rightCandlePos = [-1] * n
        pre = n
        for i in range(n - 1,-1,-1):
            if s[i] == '|':
                pre = i
            rightCandlePos[i] = pre
        #print(rightCandlePos)
        # 前缀和
        preSum = [0]
        for c in s:
            if c == '*':
                preSum.append(preSum[-1] + 1)
            else:
                preSum.append(preSum[-1])
        #print(preSum)

        qn = len(queries)
        ans = [0] * qn
        for i,(s,e) in enumerate(queries):
            l = rightCandlePos[s]
            r = leftCandlePos[e]
            #print(l,r)
            # l >= 0 和 r >= 0是为了防止出界
            # r > l是为了防止结果小于0
            if l >= 0 and r >= 0 and r > l:
                ans[i] = preSum[r] - preSum[l]
        return ans