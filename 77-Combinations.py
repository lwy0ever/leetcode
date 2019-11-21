class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(arr,start):
            if len(arr) == k:
                ans.append(arr)
            for i in range(start,n + 1):
                dfs(arr + [i],i + 1)
        
        dfs([],1)
        return ans