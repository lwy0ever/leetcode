class Solution:
    def rob(self, nums: List[int]) -> int:
        # because house[0] and house[n - 1] is adjacent
        # we have 2 plans:
        # 1:rob 0 to n - 2
        # 2:rob 1 to n - 1
        # return the bigger one
        if len(nums) == 1:
            return nums[0]
        pre2 = pre1 = 0
        for n in nums[1:]:
            pre1,pre2 = pre2 + n,max(pre1,pre2)
            '''
            cur = pre2 + n
            pre1 = max(pre1,pre2)
            pre1,pre2 = cur,pre1
            '''
        plan1 = max(pre1,pre2)
        pre2 = pre1 = 0
        for n in nums[:-1]:
            pre1,pre2 = pre2 + n,max(pre1,pre2)
        plan2 = max(pre1,pre2)
        return max(plan1,plan2)   