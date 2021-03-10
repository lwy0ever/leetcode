class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp
        n = len(nums)
        dp = [x for x in nums]    # dp[i]表示包含元素nums[i]的情况下,可以获得的最大值
        arr = [(dp[0],0)] # 存储前k - 1个dp的值和位置,降序,较小的数字直接弹出
        for i in range(1,n):
            m = arr[0][0]   # m表示前面k - 1个dp的最大值
            dp[i] = max(dp[i],m + nums[i])
            while arr and dp[i] >= arr[-1][0]:
                arr.pop()
            arr.append((dp[i],i))
            while arr[0][1] <= i - k:
                arr.pop(0)
            #print(arr)
        return max(dp)