class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # 要求子序列和大于总和的一半
        # 为了"长度最小",从最大的数字开始取
        # 为了"元素之和最大",更需要从最大的数字开始取
        s = sum(nums)
        nums.sort(reverse = True)
        ans = list()
        sumAns = 0
        for n in nums:
            ans.append(n)
            sumAns += n
            if sumAns * 2 > s:
                return ans