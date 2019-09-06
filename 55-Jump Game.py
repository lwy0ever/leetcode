class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #倒叙法
        '''
        n = len(nums)
        if n == 1:
            return True
        zeroNum = 0
        for i in range(n - 2,0,-1):
            if zeroNum > 0:
                if nums[i] > zeroNum:
                    zeroNum = 0
                else:
                    zeroNum += 1
            elif nums[i] == 0:
                zeroNum = 1
        #print(target)
        return nums[0] > zeroNum
        '''
        #正序法
        n = len(nums)
        p = 0
        maxRange = nums[p]
        while maxRange < n - 1 and p <= maxRange:
            maxRange = max(maxRange,p + nums[p])
            print(p,maxRange)
            p += 1
        return maxRange >= n - 1
