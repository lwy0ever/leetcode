from collections import defaultdict
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        length = len(s)
        base = ord('a')
        dic = 0
        dp = [0]
        for c in s:
            dic ^= 1 << (ord(c) - base)
            dp.append(dic)
        #print(dp)
        
        for l,r,k in queries:
            n = dp[r + 1] ^ dp[l]
            r = 0
            while n != 0:
                n &= n - 1
                r += 1
            ans.append(r // 2 <= k)
        return ans