class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        ans = []
        for a in arr:
            if len(ans) < k:
                heapq.heappush(ans,-a)
            else:
                if -ans[0] > a:
                    heapq.heappop(ans)
                    heapq.heappush(ans,-a)
            #print(ans)
        return [-x for x in ans]
        '''
        arr.sort()
        return arr[:k]
        '''