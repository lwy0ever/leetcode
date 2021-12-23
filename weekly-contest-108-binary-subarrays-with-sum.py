class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 滑动窗口,窗口左侧[left1,left2)是0
        # i标记右侧1的结束位置
        # left1 <= left2 <= i + 1
        left1 = 0
        left2 = 0
        s1 = 0  # left1到i的窗口和
        s2 = 0  # left2到i的窗口和
        ans = 0
        n = len(nums)
        for i in range(n):
            s1 += nums[i]
            s2 += nums[i]
            while left1 <= i and s1 > goal:
                s1 -= nums[left1]
                left1 += 1
            while left2 <= i and s2 >= goal:
                s2 -= nums[left2]
                left2 += 1
            ans += left2 - left1
        return ans