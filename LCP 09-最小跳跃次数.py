class Solution:
    def minJump(self, jump: List[int]) -> int:
        # bfs
        n = len(jump)
        visited = [False] * n
        visited[0] = True
        fromP = [0]
        _min = -1   # 不用再检查_min及之前的部分
        ans = 0
        while fromP:
            ans += 1
            toP = []
            _max = max(fromP)
            for i in range(_min + 1,_max + 1):
                if visited[i] == False:
                    toP.append(i)
                    visited[i] = True
            for f in fromP:
                if f + jump[f] >= n:
                    return ans
                if visited[f + jump[f]] == False:
                    toP.append(f + jump[f])
                    visited[f + jump[f]] = True
            _min = _max
            fromP = toP
            #print(ans,_min,_max,fromP)