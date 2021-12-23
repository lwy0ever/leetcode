class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l
        
        # 低效算法
        ans = len(nums)
        i = 0
        while i < ans:
            if nums[i] == val:
                nums.pop(i)
                ans -= 1
            else:
                i += 1
        return ans