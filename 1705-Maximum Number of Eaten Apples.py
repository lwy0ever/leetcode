class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # arr[i] = [day,quantity]
        # day表示苹果的有效期,quantity表示苹果的数量
        # 由于有效期是一次性清零的,所以按照day排序
        
        # 处理分2部分
        # 1,在0到n - 1天,优先吃最早坏掉的
        # 2,在n天及以后
        ans = 0
        n = len(apples)
        arr = []
        # 0到n - 1天
        for i in range(n):
            while arr and arr[0][0] <= i:   # 扔掉坏苹果
                heappop(arr)    # 小根堆
            if apples[i] > 0:  # 有新的苹果,入堆
                heappush(arr,[i + days[i],apples[i]])
            if arr: # 尝试吃苹果
                arr[0][1] -= 1  # 因为坏苹果已经扔了,有就可以吃
                if arr[0][1] == 0:
                    heappop(arr)
                ans += 1
        i = n
        # n天及以后
        while arr:
            while arr and arr[0][0] <= i:   # 扔掉坏苹果
                heappop(arr)
            if not arr: # 没有了,结束
                break
            day,apple = heappop(arr)
            num = min(day - i,apple)    # 这批苹果可以吃num天
            ans += num
            i += num
        return ans