class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(colors)
        d = [[n] * 3 for _ in range(n)]
        #print(d)
        pre = [-n] * 3
        for i in range(n):
            pre[colors[i] - 1] = i
            for j in range(3):
                d[i][j] = i - pre[j]
        pre2 = [n * 2] * 3
        for i in range(n - 1,-1,-1):
            pre2[colors[i] - 1] = i
            for j in range(3):
                if pre[j] == -n:
                    continue
                d[i][j] = min(d[i][j],pre2[j] - i)
        for q in queries:
            if pre[q[1] - 1] == -n:
                ans.append(-1)
            else:
                ans.append(d[q[0]][q[1] - 1])
        return ans