class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        dic = {}
        for n in nums:
            if n in dic: continue
            left = dic.get(n - 1,0)
            right = dic.get(n + 1,0)
            dic[n] = left + right + 1
            dic[n - left] = dic[n]
            dic[n + right] = dic[n]
            #print(dic)
            ans = max(ans,dic[n])
        return ans 