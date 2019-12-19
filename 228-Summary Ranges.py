class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = [[nums[0],nums[0]]]
        for n in nums[1:]:
            if ans[-1][1] + 1 == n:
                ans[-1][1] = n
            else:
                ans.append([n,n])
        ansStr = []
        for a,b in ans:
            if a == b:
                ansStr.append(str(a))
            else:
                ansStr.append(str(a) + '->' + str(b))
        return ansStr