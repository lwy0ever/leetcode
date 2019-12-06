class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        # 类似桶排序
        # 有n个数字，所以有n - 1个gap
        # 从min到max,分n - 1个桶,每个桶的宽度是ceil((max - min) / (n - 1))
        # 桶i的range是左闭右开区间:[min + ceil((max - min) / (n - 1)) * i,min + ceil((max - min) / (n - 1)) * (i + 1))
        # 每个桶内元素差一定小于ceil((max - min) / (n - 1))
        # bucket[i][0]表示桶内最小值
        # bucket[i][0]表示桶内最大值
        mi = min(nums)
        ma = max(nums)
        r = math.ceil((ma - mi) / (n - 1))  # range
        bucket = [[float('inf'),float('-inf')] for _ in range(n - 1)]
        for num in nums:
            # 跳过边界,尤其是num == ma时的边界
            if num == ma:
                continue
            i = (num - mi) // r
            bucket[i][0] = min(bucket[i][0],num)
            bucket[i][1] = max(bucket[i][1],num)
        #print(bucket)
        ans = 0
        preMax = mi
        for iMin,iMax in bucket:
            #print(preMax,iMin,iMax)
            if iMin != float('inf'):
                ans = max(ans,iMin - preMax)
                preMax = iMax
        ans = max(ans,ma - preMax)
        return ans