class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return list(itertools.permutations(nums))

        used = set()
        n = len(nums)
        ans = [[nums[0]]]
        for i in range(1,n):
            new_ans = []
            an = len(ans[0])
            for a in ans:
                for j in range(an + 1):
                    new_ans.append(a[:j] + [nums[i]] + a[j:])
            ans = new_ans
        return ans