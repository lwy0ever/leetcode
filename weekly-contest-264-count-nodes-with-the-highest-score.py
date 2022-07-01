class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # 一个点,有6种连接情况
        # 1,有父,无子   结果=n - 1
        # 2,有父,有1子  结果=(n - 1 - 子树) * 子树
        # 3,有父,有2子  结果=(n - 1 - 子树1 - 子树2) * 子树1 * 子树2
        # 4,无父,无子   由于n >= 2,不存在这种情况
        # 5,无父,有1子  结果=n - 1
        # 6,无父,有2子  结果=子树1 * 子树2
        n = len(parents)
        children = [[] for _ in range(n)]
        for i,p in enumerate(parents[1:],start = 1):
            children[p].append(i)
        #print(children)
        subTree = [[] for _ in range(n)]    # 子树的节点数量
        
        def countSub(node):
            for c in children[node]:
                subTree[node].append(countSub(c))
            return sum(subTree[node]) + 1
        
        countSub(0)
        #print(subTree)

        ans = 0
        maxValue = 0
        for i in range(n):
            f = n - 1 - sum(subTree[i])
            #print(i,f,subTree[i])
            fx = max(f,1)
            if len(subTree[i]) == 0:
                v  = fx
            elif len(subTree[i]) == 1:
                v = fx * subTree[i][0]
            elif len(subTree[i]) == 2:
                v = fx * subTree[i][0] * subTree[i][1]
            if v > maxValue:
                maxValue = v
                ans = 1
            elif v == maxValue:
                ans += 1
        return ans
        '''
        ans = collections.defaultdict(int)
        for i in range(n):
            f = n - 1 - sum(subTree[i])
            #print(i,f,subTree[i])
            fx = max(f,1)
            if len(subTree[i]) == 0:
                ans[fx] += 1
            elif len(subTree[i]) == 1:
                ans[fx * subTree[i][0]] += 1
            elif len(subTree[i]) == 2:
                ans[fx * subTree[i][0] * subTree[i][1]] += 1
            #print(ans)
        return ans[max(ans.keys())]
        '''