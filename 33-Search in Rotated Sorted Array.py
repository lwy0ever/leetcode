class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找,l means left,r means right
        # 注意target和nums[i]的开闭区间问题
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            #print(l,m,r,nums[l],nums[m],nums[r])
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:   # 左侧升序
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:   # 右侧升序
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1