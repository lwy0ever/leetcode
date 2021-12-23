class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bfs
        # 无脑飞
        ans = float('inf')
        price = [float('inf')] * n
        price[src] = 0
        for _ in range(k + 1):
            newPrice = [float('inf')] * n
            for f,t,p in flights:
                newPrice[t] = min(newPrice[t],price[f] + p)
            price = newPrice
            ans = min(ans,price[dst])
        return -1 if ans == float('inf') else ans
        
        '''
        # bfs
        # 可能出现到达某一节点的中转次数多,但是花费少的情况,所以不能用visited判断
        ans = float('inf')
        direct = collections.defaultdict(dict)
        for f,t,p in flights:
            direct[f][t] = p
        fromP = {src:0}
        #visited = {src:0}
        for _ in range(k + 1):  # 中转k次,所以乘坐k + 1次航班
            toP = dict()
            for f,p in fromP.items():
                for t,newP in direct[f].items():
                    # 新目的地的花费,可以是已有的花费
                    # 也可以是新的一次转机形成
                    toP[t] = min(toP.get(t,float('inf')),p + newP)
            fromP = toP
            ans = min(ans,fromP.get(dst,float('inf')))
        return -1 if ans == float('inf') else ans
        '''