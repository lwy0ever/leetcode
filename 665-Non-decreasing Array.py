class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                if cnt > 1:
                    return False
                # i < n - 2 and nums[i] > nums[i + 2],这种情况,修改nums[i]是有救的
                # i + 1 > 1 and nums[i - 1] > nums[i + 1],这种情况,修改nums[i + 1]是有救的
                # 如果上述2种情况同时发生,就无解了
                if i < n - 2 and nums[i] > nums[i + 2] and i + 1 > 1 and nums[i - 1] > nums[i + 1]:
                    return False
        return cnt <= 1