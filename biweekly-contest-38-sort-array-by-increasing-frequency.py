class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = collections.Counter(nums)
        for v,c in sorted(cnt.most_common(),key = lambda x:(x[1],-x[0])):
            ans += [v] * c
        return ans