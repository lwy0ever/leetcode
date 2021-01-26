class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        linked = [0] * n
        s = set()
        for a,b in roads:
            linked[a] += 1
            linked[b] += 1
            s.add((a,b))
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1,n):
                ttl = linked[i] + linked[j]
                if (i,j) in s or (j,i) in s:
                    ttl -= 1
                ans = max(ans,ttl)
        return ans