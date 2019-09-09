class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = {}
        posStart = {}
        posEnd = {}
        for i in range(len(nums)):
            if nums[i] in cnt:
                cnt[nums[i]] += 1
            else:
                cnt[nums[i]] = 1
                posStart[nums[i]] = i
            posEnd[nums[i]] = i
        ma = max(cnt.values())
        ans = float('inf')
        for k in cnt:
            if cnt[k] == ma:
                ans = min(ans,posEnd[k] - posStart[k] + 1)
        return ans
        '''
        ma = 0
        ans = float('inf')
        for k,v in sorted(cnt.items(),key = lambda x:x[1],reverse = True):
            if v < ma:
                break
            ma = v
            ans = min(ans,posEnd[k] - posStart[k] + 1)
        return ans
        '''