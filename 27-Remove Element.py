class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = len(nums)
        i = 0
        while i < ans:
            if nums[i] == val:
                nums.pop(i)
                ans -= 1
            else:
                i += 1
        return ans