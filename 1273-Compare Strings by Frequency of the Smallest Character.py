from collections import Counter
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            cnt = Counter(s)
            return cnt[sorted(cnt.keys())[0]]
        
        ws = []
        for w in words:
            ws.append(f(w))
        ws.sort(reverse = True)
        dp = [0] * 12
        for w in ws:
            dp[w] += 1
        #(dp)
        for i in range(9,-1,-1):
            dp[i] += dp[i + 1]
        #print(ws)
        #print(dp)
        
        ans = []
        for q in queries:
            ans.append(dp[f(q) + 1])
        return ans