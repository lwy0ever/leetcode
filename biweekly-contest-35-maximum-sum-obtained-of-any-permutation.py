class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        # 定义一个数组pre,记录requests的重叠情况
        pre = [0] * (n + 1)
        for s,e in requests:
            pre[s] += 1
            pre[e + 1] -= 1
        # pre的前缀和就是nums[i]出现的次数
        for i in range(1,n):
            pre[i] += pre[i - 1]
        #print(pre)
        pre.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        for i in range(n):
            ans += nums[i] * pre[i]
        return ans % (10 ** 9 + 7)