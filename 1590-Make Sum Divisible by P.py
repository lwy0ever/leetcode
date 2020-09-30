class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        s = sum(nums)
        target = s % p
        if target == 0:
            return 0
        ans = float('inf')
        pre = 0
        di = {0:-1}  # 记录余数的位置
        for i,num in enumerate(nums):
            pre += num
            mi = pre % p
            di[mi] = i
            needed = p * (mi < target) + mi - target
            if needed in di:
                ans = min(ans,i - di[needed])
        return ans if ans < n else -1