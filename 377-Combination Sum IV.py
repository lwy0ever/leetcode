class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1) # dp[i]表示组成i的可能组合数
        # 这一步很关键,想想为什么 dp[0] 是 1
        # 因为 0 表示空集,空集和它"前面"的元素凑成一种解法,所以是 1
        dp[0] = 1
        nums.sort()
        for i in range(1,target + 1):
            for n in nums:
                if i < n:
                    break
                dp[i] += dp[i - n]
        print(dp)
        return dp[-1]