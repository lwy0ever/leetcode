class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if i == n:
                return i
        return -1