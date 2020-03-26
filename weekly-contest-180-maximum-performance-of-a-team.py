class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # 当两种方案的efficiency相等时,speed之和更大的方案显然更优
        # 题目的输入决定了最多有 n 种 efficiency
        # 对于每种 efficiency 肯定都会存在最优的方案
        # 最终答案肯定就是这个n种方案里面最优的那个
        # 问题转化成了如何快速求出每种 efficiency 的最优方案
        arr = [(speed[i],efficiency[i]) for i in range(n)]
        arr.sort(key = lambda x:-x[1])  # 高效率的排在前面
        #print(arr)
        q = []  # speed的小根堆
        ans = 0
        _sum = 0    # 当前speed的和
        for s,e in arr:
            if len(q) == k:
                minSpeed = heapq.heappop(q)    # 当前speed的最小值
                _sum -= minSpeed
            else:
                minSpeed = 0
            heapq.heappush(q,max(minSpeed,s))   # 找一个speed更高的员工加入
            _sum += max(minSpeed,s)
            ans = max(ans,e * _sum)
        return ans % (10 ** 9 + 7)