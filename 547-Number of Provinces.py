class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs
        n = len(isConnected)
        visited = set()
        
        def dfs(i): # 把和i相关的都连接起来
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        ans = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                ans += 1
        return ans