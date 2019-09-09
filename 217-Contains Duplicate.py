class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for n in nums:
            if n in exists:
                return True
            exists.add(n)
        return False