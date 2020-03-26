class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 在分组最大值为m的情况下,分组的数量
        def cntGroup(_max):
            s = 0   # 当前组内数字和
            cnt = 1 # 当前组数
            for n in nums:
                if s + n > _max:   # 超过最大值,需要新建分组
                    cnt += 1
                    s = n
                else:   # 归入当前组
                    s += n
            return cnt                    

        left,right = max(nums),sum(nums)    # 二分查找的上下标,表示每个分组的最大值
        while left < right:
            mid = (left + right) // 2
            if cntGroup(mid) <= m:  # 注意cntGroup(mid) == m的情况下,应该尝试减少
                right = mid
            else:
                left = mid + 1
        return left
        