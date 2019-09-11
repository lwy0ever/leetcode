class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ex = set()
        s = 0
        pre = 0
        for num in nums:
            s += num
            if k != 0:
                s %= k
            if s in ex:
                return True
            ex.add(pre)
            pre = s
        return False