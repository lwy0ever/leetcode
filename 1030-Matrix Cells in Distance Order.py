class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 方法1:排序
        ans = []
        for i in range(R):
            for j in range(C):
                ans.append([i,j])
        ans.sort(key = lambda x:abs(x[0] - r0) + abs(x[1] - c0))
        return ans

        '''
        # 方法2:bfs
        ans = [[r0,c0]]
        # bfs
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        fromP = [(r0,c0)]
        visited = {(r0,c0)}
        while fromP:
            toP = []
            for fr,fc in fromP:
                for dr,dc in di:
                    if 0 <= fr + dr < R and 0 <= fc + dc < C and (fr + dr,fc + dc) not in visited:
                        visited.add((fr + dr,fc + dc))
                        toP.append((fr + dr,fc + dc))
                        ans.append([fr + dr,fc + dc])
            fromP = toP
        return ans
        '''