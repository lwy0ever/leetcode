class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # 堆
        n = len(arr)
        #print(n)
        n5 = n // 20
        heapMin = list()    # 大根堆,存负数
        minCnt = 0
        heapMax = list()    # 小根堆
        maxCnt = 0
        for a in arr:
            if minCnt < n5:
                heapq.heappush(heapMin,-a)
                minCnt += 1
            elif -a > heapMin[0]:
                heapq.heapreplace(heapMin,-a)
            if maxCnt < n5:
                heapq.heappush(heapMax,a)
                maxCnt += 1
            elif a > heapMax[0]:
                heapq.heapreplace(heapMax,a)
            #print(heapMin,heapMax,minCnt,maxCnt)
        return (sum(arr) + sum(heapMin) - sum(heapMax)) / (n - n5 * 2)