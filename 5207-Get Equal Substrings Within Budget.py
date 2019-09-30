class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = []
        cc = 0
        l = 0
        ans = 0
        for i in range(n):
            cost.append(abs(ord(s[i]) - ord(t[i])))
            cc += cost[-1]
            while l <= i and cc > maxCost:
                cc -= cost[l]
                l += 1
            ans = max(ans,i - l + 1)
        return ans