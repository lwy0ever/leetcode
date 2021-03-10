class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # 要求的是最大数目,所以有满足条件的,就应该马上组成
        ans = 0
        pre = {0} # 记录之前出现的和
        s = 0
        for n in nums:
            s += n
            #print(s,pre)
            if s - target in pre:
                ans += 1
                pre = {0}
                s = 0
            else:
                pre.add(s)
        return ans