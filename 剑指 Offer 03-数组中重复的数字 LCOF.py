class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        existed = set()
        for n in nums:
            if n in existed:
                return n
            existed.add(n)