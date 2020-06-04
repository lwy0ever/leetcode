class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 由于n <= 100,len(queries) <= 10 ** 4
        # 考虑缓存之前计算的结果
        # 方法1
        coursePre = [set() for _ in range(n)]  # 存储课程的先修课程
        for p,c in prerequisites:
            coursePre[c].add(p)
        for c in range(n):
            # bfs
            pre = coursePre[c].copy()
            while pre:
                newPre = set()
                for p in pre:
                    for np in coursePre[p]:
                        if np not in coursePre[c]:
                            coursePre[c].add(np)
                            newPre.add(np)
                pre = newPre
        ans = []
        for p,c in queries:
            ans.append(p in coursePre[c])
        return ans
        # 方法2
        '''
        dp = [[False] * n for _ in range(n)]
        for p,c in prerequisites:
            dp[p][c] = True
        #print(dp)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] and dp[k][j]:
                        dp[i][j] = True
        #print(dp)
        ans = []
        for p,c in queries:
            ans.append(dp[p][c])
        return ans
        '''