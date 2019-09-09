class Solution:
    def rob(self, nums: List[int]) -> int:
        pre2 = pre1 = 0
        for n in nums:
            pre1,pre2 = pre2 + n,max(pre1,pre2)
            '''
            cur = pre2 + n
            pre1 = max(pre1,pre2)
            pre1,pre2 = cur,pre1
            '''
        return max(pre1,pre2)        