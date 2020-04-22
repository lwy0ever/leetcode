class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        oddNum = 0
        odds = []   # 记录奇数数字的位置
        odds.append(-1) # 哨兵位
        for i in range(n):
            if nums[i] & 1:
                odds.append(i)
                oddNum += 1
        odds.append(n)   # 记录奇数数字的位置
        ans = 0
        for i in range(1,oddNum - k + 2):   # 子数组中第一个奇数的位置
            last = i + k - 1
            ans += (odds[i] - odds[i - 1]) * (odds[last + 1] - odds[last])
        return ans