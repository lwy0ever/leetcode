class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        cnt = 0
        for e in nums:
            if e < target:
                continue
            elif e == target:
                cnt += 1
            else:
                break
        return cnt * 2 > n
        