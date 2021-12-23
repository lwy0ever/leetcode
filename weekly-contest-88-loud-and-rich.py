class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # 建立一个拓扑图m
        # m[i] = list()表示比i更富有的人
        n = len(quiet)
        m = collections.defaultdict(list)
        for a,b in richer:
            m[b].append(a)

        def find(ans,i,m):
            #print('find',i,ans[i])
            if ans[i] != -1:    # 如果已经被查找过,直接返回
                return
            ans[i] = i  # 包含自身
            for r in m[i]:
                #print(ans,r,m)
                find(ans,r,m)   # 查找比自身富有的人
                if quiet[ans[i]] > quiet[ans[r]]:   # 如果比自身富有的人形成的图,更加安静,则更新
                    ans[i] = ans[r]
            #print('ans',i,ans[i])

        ans = [-1] * n
        for i in range(n):
            #print(ans,i,m)
            find(ans,i,m)   # 查找每个人,避免遗漏
        return ans