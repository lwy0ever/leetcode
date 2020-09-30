class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # 每一段长度为n的连续相同字符,删除其中n - 1个
        cost.append(0)
        pre = '.'
        pos = -1
        ans = 0
        _sum = 0    # 记录连续相同字符的删除代价
        _max = 0    # 记录代价中最大的值
        for i,c in enumerate(s + '.'):
            if c == pre:
                _sum += cost[i]
                _max = max(_max,cost[i])
            else:
                ans += _sum - _max
                pre = c
                pos = i
                _sum = cost[i]
                _max = cost[i]
            #print(i,c,pre,pos,_sum,_max,ans)
        return ans
                