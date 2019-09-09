class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            b = bin(i)[2:].zfill(n)
            one = []
            for c in range(n):
                if b[c] == '1':
                    one.append(nums[c])
            ans.append(one)
        return ans
        