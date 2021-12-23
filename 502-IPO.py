class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        # 一个排序数组,按照需要的资金对项目排序,指针cur指向当前最大的可选范围
        # 一个大根堆,按照收益排序
        # 每次从大根堆里选根(最大收益)加入总资本,然后cur移动,扩大可选范围
        if W > max(Capital):    # 不差钱,任何一项投资钱都够
            return W + sum(sorted(Profits,reverse = True)[:k])
        
        n = len(Profits)
        cp = sorted(zip(Capital,Profits))
        pq = []
        cur = 0
        for _ in range(k):
            while cur < n and cp[cur][0] <= W:
                heappush(pq,-cp[cur][1])
                cur += 1
            if pq:  # 有项目可以投
                W -= heappop(pq)   # 因为是大根堆,存的负收益,所以用-=
            else:
                break
        return W
        
        # 会超时
        '''
        pc = sorted(zip(Profits,Capital),reverse = True)
        #print(pc)
        ans = 0
        for _ in range(k):
            for i,v in enumerate(pc):
                #print(i,v)
                if v[1] <= W:
                    W += v[0]
                    pc.pop(i)
                    break
            else:
                break
        return W
        '''