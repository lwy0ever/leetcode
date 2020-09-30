class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(arr,start): # 已经形成了数组arr,从数字start开始考虑
            l = len(arr)
            if l == k:
                ans.append(arr)
                return
            for i in range(start,n + 1 - (k - l - 1)):
                dfs(arr + [i],i + 1)
        
        dfs([],1)
        return ans