class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pre1 = float('inf')
        pre2 = float('inf')
        for n in nums:
            if n > pre2:
                return True
            if n < pre1:
                pre1 = n
            elif n > pre1:
                if n < pre2:
                    pre2 = n
        return False