class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # 如果一组员工(可以是1个),离开的楼=入驻的楼,且每个楼需要的数量都是1,则这组员工可以被满足
        # 有一种情况[0,2],[0,1],[1,2],[2,0]
        #  选择0,3或者1,2,3,都可以满足.但是1,2,3才是最优解,而0,3不是
        ans = 0
        rn = len(requests)
        
        # 将requests中f == t的删掉,并将结果+1
        i = 0
        while i < len(requests):
            if requests[i][0] == requests[i][1]:
                requests.pop(i)
                ans += 1
            else:
                i += 1
        
        # 如果某个楼的入驻请求为0或者离开请求为0,则该楼必然不平衡,可以删除和这个楼相关的请求
        # 重复这个过程,直到删无可删
        goon = True
        while goon:
            toRemove = set()
            buildRefer = [set() for _ in range(n)]
            rIn = [0] * n
            rOut = [0] * n
            for i,(f,t) in enumerate(requests):
                rOut[f] += 1
                rIn[t] += 1
                buildRefer[f].add(i)
                buildRefer[t].add(i)
            #print(requests,buildRefer)
            goon = False
            for i in range(n):
                if (rOut[i] > 0 and rIn[i] == 0) or (rOut[i] == 0 and rIn[i] > 0):
                    #print(sorted(buildRefer[i],reverse = True))
                    for r in buildRefer[i]:
                        toRemove.add(r)
            if toRemove:
                goon = True
            for r in sorted(toRemove,reverse = True):
                requests.pop(r)
        
        # 用组合
        rn = len(requests)
        for l in range(rn,0,-1):
            for c in itertools.combinations(requests,l):
                degree = [0] * n
                for f,t in c:
                    degree[f] -= 1
                    degree[t] += 1
                if not any(degree):
                    return ans + l
        return ans
        '''
        # 类似dp,穷举
        zero = tuple([0] * n)
        # 考虑requests[i],目标状态为stat的最大解
        cache = dict()
        def dp(i,stat):
            if (i,stat) in cache:
                return cache[(i,stat)]
            if i == len(requests):
                if stat == zero:
                    return 0
                else:
                    return float('-inf')
            newStat = list(stat)
            newStat[requests[i][0]] += 1
            newStat[requests[i][1]] -= 1
            # 不选择i or 选择i
            ans = max(dp(i + 1,stat),dp(i + 1,tuple(newStat)) + 1)
            cache[(i,stat)] = ans
            return ans
        return dp(0,zero) + ans
        '''