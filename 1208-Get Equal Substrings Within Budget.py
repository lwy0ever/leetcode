class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 方法1:
        n = len(s)
        cost = [0] * n
        for i in range(n):
            cost[i] = abs(ord(s[i]) - ord(t[i]))
        cc = 0
        l = 0
        ans = 0
        for i in range(n):
            cc += cost[i]
            while l <= i and cc > maxCost:
                cc -= cost[l]
                l += 1
            ans = max(ans,i - l + 1)
        return ans

        # 方法2:
        # 设定s[l:r + 1]的总开销为ttl
        # 当ttl + diff[r] > maxCost时,l + 1
        # 当ttl + diff[r] <= maxCost时,r + 1
        ans = 0
        n = len(s)
        cost = [0] * n
        for i in range(n):
            cost[i] = abs(ord(s[i]) - ord(t[i]))
        l = 0
        r = 0
        ttl = 0
        while r < n:
            if ttl + cost[r] > maxCost:
                ttl -= cost[l]
                l += 1
            else:   # ttl + diff[r] <= maxCost
                ttl += cost[r]
                r += 1
                ans = max(ans,r - l)
            #print(l,r,ttl,ans)
        return ans