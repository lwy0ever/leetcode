class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        _max = 0    # 可以到达的最远位置
        for i in range(n):
            if i > _max:
                return False
            _max = max(_max,i + nums[i])
            #print(i,nums[i],_max)
            if _max >= n - 1:
                return True
        return False