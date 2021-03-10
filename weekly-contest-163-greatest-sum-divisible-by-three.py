class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s
        #print(s)
        ans = 0
        nums.sort()
        s1 = []
        s2 = []
        for n in nums:
            #print(n,s1,s2,ans)
            if n % 3 == 0:
                continue
            elif n % 3 == 1:
                if len(s1) < 2:
                    s1.append(n)
            elif n % 3 == 2:
                if len(s2) < 2:
                    s2.append(n)
            if s % 3 == 1:
                if len(s1) >= 1:
                    ans = max(ans,s - s1[0])
                if len(s2) >= 2:
                    ans = max(ans,s - s2[0] - s2[1])
            elif s % 3 == 2:
                if len(s2) >= 1:
                    ans = max(ans,s - s2[0])
                if len(s1) >= 2:
                    ans = max(ans,s - s1[0] - s1[1])
        return ans