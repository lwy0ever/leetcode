class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans[i] = nums[i]左侧所有元素的乘积 x nums[i]右侧所有元素的乘积
        n = len(nums)
        ans = [1] * n
        # 计算左侧元素乘积
        for i in range(1,n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # 计算右侧元素乘积,并合并到ans中
        t = 1
        for i in range(n - 1,-1,-1):
            ans[i] *= t
            t *= nums[i]
        #print(ans)
        return ans