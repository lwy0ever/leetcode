class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 把unavailable的list换成heapq
        from sortedcontainers import SortedSet
        # 空闲的服务器
        # 排序为了快速查找
        # set为了快速add和remove
        available = SortedSet({i for i in range(k)})
        unavailable = list()    # 存储(时间,服务器编号),小根堆
        #print(available)
        cnt = [0] * k   # 记录每个服务器被使用的次数
        for i,(a,l) in enumerate(zip(arrival,load)):
            while unavailable and unavailable[0][0] <= a:
                _,serverID = heapq.heappop(unavailable)
                available.add(serverID)
            n = len(available)
            if n == 0:
                continue
            start = i % k
            pos = bisect.bisect_left(available,start)
            if pos == n:
                pos = 0
            serverID = available[pos]
            available.remove(serverID)
            heapq.heappush(unavailable,(a + l,serverID))
            cnt[serverID] += 1
            #print(available,unavailable,cnt)
        _max = max(cnt)
        ans = []
        for i in range(k):
            if cnt[i] == _max:
                ans.append(i)
        return ans
        '''
        from sortedcontainers import SortedSet
        # 空闲的服务器
        # 排序为了快速查找
        # set为了快速add和remove
        available = SortedSet({i for i in range(k)})
        unavailable = list()    # 存储(-时间,服务器编号),时间的负数为了方便排序,同时可以pop
        #print(available)
        cnt = [0] * k   # 记录每个服务器被使用的次数
        for i,(a,l) in enumerate(zip(arrival,load)):
            while unavailable and unavailable[-1][0] >= - a:
                _,serverID = unavailable.pop()
                available.add(serverID)
            n = len(available)
            if n == 0:
                continue
            start = i % k
            pos = bisect.bisect_left(available,start)
            if pos == n:
                pos = 0
            serverID = available[pos]
            available.remove(serverID)
            bisect.insort_left(unavailable,(- a - l,serverID))
            cnt[serverID] += 1
            #print(available,unavailable,cnt)
        _max = max(cnt)
        ans = []
        for i in range(k):
            if cnt[i] == _max:
                ans.append(i)
        return ans
        '''