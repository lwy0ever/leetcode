class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valPos = {} # valPos[v]表示v最后出现的位置
        n = len(nums)
        for i in range(n):
            if nums[i] in valPos and i - valPos[nums[i]] <= k:
                return True
            valPos[nums[i]] = i
        return False