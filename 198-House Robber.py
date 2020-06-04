class Solution:
    def rob(self, nums: List[int]) -> int:
        preRob = 0  # 表示抢劫上一家
        noPreRob = 0 # 表示不抢劫上一家
        for n in nums:
            preRob,noPreRob = noPreRob + n,max(preRob,noPreRob)
            #print(preRob,noPreRob)
        return max(preRob,noPreRob)