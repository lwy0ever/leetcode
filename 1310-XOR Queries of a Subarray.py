class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] ^ arr[i]
        ans = []
        for s,e in queries:
            ans.append(dp[e + 1] ^ dp[s])
        return ans