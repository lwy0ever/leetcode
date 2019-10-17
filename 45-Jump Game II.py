class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        #for i,v in enumerate(nums):
        #    nums[i] = i + nums[i]
        ans = 0
        ma = 0 # 表示已经经过的部分可以跳到的最远处
        macur = 0 # 表示当前这一跳可以跳到的最远处
        for i,num in enumerate(nums):
            v = i + num
            # 需要达到i,必须增加一跳
            if i > macur:
                ans += 1
                macur = ma
            # 可以跳到的最远处
            if v > ma:
                if v >= n - 1:
                    ans += 1
                    break
                ma = v
            #print(i,ans,macur,ma)
        return ans