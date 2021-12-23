class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        # 排序之后 如果 i<j<k 如果 num[j] % num[i] == 0
        # 而且 num[k] % num[j] == 0
        # 那么 num[k] % num[i]必然也是0
        nums.sort()
        dp = [1] * n    #dp[i]表示nums[0:i]中可以被nums[i]整除的数量(自己可以被自己整除)
        pre = [-1] * n  #pre[i]表示nums[i]的前一个元素，也就是nums[i] % nums[pre[i]] == 0
        maxNum = 0
        maxIndex = 0
        for i in range(1,n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j
                        if dp[i] > maxNum:
                            maxNum = dp[i]
                            maxIndex = i
        #print(nums)
        #print(dp)
        #print(pre)
        #print(maxIndex)
        ans = []
        p = maxIndex
        while p >= 0:
            ans.append(nums[p])
            p = pre[p]
        return ans