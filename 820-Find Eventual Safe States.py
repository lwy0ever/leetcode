class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        ind = collections.defaultdict(list) # 反向路径
        for i in range(len(graph)):
            if not graph[i]:
                ans += [i]
            for j in graph[i]:
                ind[j].append(i)
        #print(ans)
        for j in ans:
            #print(j)
            for i in ind[j]:
                # 如果一个节点的后续节点都安全，则该节点安全
                # 安全路径可以被删除
                graph[i].remove(j)
                if not graph[i]:
                    ans += [i]
        return sorted(ans)
                