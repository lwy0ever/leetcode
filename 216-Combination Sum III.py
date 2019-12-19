class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def dfs(k,n,arr):
            if k == 0 and n == 0:
                nonlocal ans
                ans.append(arr)
            if k < 0 or (arr and n <= arr[-1]):
                return
            if arr:
                st = arr[-1] + 1
            else:
                st = 1
            for i in range(st,10):
                dfs(k - 1,n - i,arr + [i])
        
        dfs(k,n,[])
        return ans