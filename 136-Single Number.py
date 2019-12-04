class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 模拟二进制
        ans = 0
        for n in nums:
            ans ^= n
        return ans