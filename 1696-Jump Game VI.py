class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = []   # 存放出现的最大值和位置
        ans = nums[0]
        heapq.heappush(h,(-nums[0],0))
        for i in range(1,n):
            while h and h[0][1] + k < i:  # 把无效的大数字弹出
                heapq.heappop(h)
            ans = -h[0][0] + nums[i]
            heapq.heappush(h,(-ans,i))
        return ans