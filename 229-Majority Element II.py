class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        # 投票法
        # 先选出2个得票最多的候选人
        uA = nums[0]
        cntA = 0
        uB = nums[0]
        cntB = 0
        for x in nums:
            if x == uA:
                cntA += 1
                continue    # 解决uA == uB的情况
            if x == uB:
                cntB += 1
                continue    # 解决uA == uB的情况
            if cntA == 0:
                uA = x
                cntA = 1
                continue    # 由于更换了候选人,相当于候选人票数增加,所以另外一个候选人的票数不用减少
            if cntB == 0:
                uB = x
                cntB = 1
                continue
            # 未更换候选人,当前每个候选人票数差距减小
            cntA -= 1
            cntB -= 1
        cntA = 0
        cntB = 0
        # 统计数量
        for x in nums:
            if x == uA:
                cntA += 1
            elif x == uB:   # 避免uA == uB的情况
                cntB += 1
        ans = []
        if cntA > n // 3:
            ans.append(uA)
        if cntB > n // 3:
            ans.append(uB)
        return ans