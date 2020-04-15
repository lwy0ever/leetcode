class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        canP = {0}
        s = sum(nums)
        if s & 1:
            return False
        target = s // 2
        for n in nums:
            newCan = set()
            for c in canP:
                if c + n <= target:
                    newCan.add(c + n)
            if target in canP:
                return True
            canP.update(newCan)
        return False