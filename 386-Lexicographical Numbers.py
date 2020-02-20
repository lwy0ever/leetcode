class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur):
            #print(cur,n)
            ans.append(cur)
            for i in range(10):
                if cur * 10 + i > n:
                    return
                dfs(cur * 10 + i)
        
        ans = []
        for i in range(1,10):
            if i > n:
                break
            dfs(i)
        return ans