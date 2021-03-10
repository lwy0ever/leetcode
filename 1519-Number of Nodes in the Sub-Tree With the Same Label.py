class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d = collections.defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        ans = [0] * n
        visited = set()
        
        def dfs(i): # 返回所有子树的标签数量
            visited.add(i)
            cnt = collections.Counter({})   # 这里一定要{},确保会新生成一个Counter
            for t in d[i]:
                if t not in visited:
                    cnt += dfs(t)
            cnt[labels[i]] += 1 # 包含自身
            #print(i,cnt,id(cnt))
            ans[i] = cnt[labels[i]]
            return cnt
        
        dfs(0)
        return ans