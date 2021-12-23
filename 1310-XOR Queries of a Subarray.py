class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        x = 0
        for a in arr:
            x ^= a
            pre.append(x)
        ans = []
        for s,t in queries:
            ans.append(pre[s] ^ pre[t + 1])
        return ans