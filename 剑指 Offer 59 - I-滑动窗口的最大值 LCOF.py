class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 考虑nums[i],i > k
        # 在nums[i - k:i]中,所有比nums[i]小的数都将不起作用,可以弹出
        # 此时nums[i]是最小的,放在队列最左侧
        def clearDeque(i):  # 将deque中小于nums[i]的弹出
            # 如果i - k是当前最大值,则需要弹出
            # 否则,无需理会
            # 那么,会不会有i < j,nums[d[i]] > nums[d[j]],d[i]先被弹出,而d[j]无法被弹出的情况呢?
            # 假设d[j] < d[i],由于nums[d[i]] > nums[d[j]]
            # 在扫描d[0]的时候,先扫描到i,j没有被扫描到
            # 但是由于nums[d[i]] > nums[d[j]],d[i]被插入的时候,d[j]已经被弹出了
            if d and d[0] == i - k:
                d.popleft()
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            #print(d)

        d = collections.deque()  # 存放nums的下标,按照nums[i]从大到小排序
        n = len(nums)
        ans = []
        for i in range(n):
            clearDeque(i)
            d.append(i)
            #print(d)
            if i >= k - 1:
                ans.append(nums[d[0]])
        return ans