class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 为了减少内存占用,使用dfs
        ans = []
        dst = len(graph) - 1
        def dfs(path):
            for nextNode in graph[path[-1]]:
                path.append(nextNode)
                if nextNode == dst:
                    ans.append(path.copy())
                dfs(path)
                path.pop()
        
        dfs([0])
        return ans