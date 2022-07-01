class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        from functools import reduce
        _max = reduce(lambda x,y:x | y,nums)
        n = len(nums)
        ans = 0
        
        def t(already,i):
            #print(already,i)
            if already == _max:
                nonlocal ans
                ans += 2 ** (n - i)
                #print(ans)
            else:
                if i >= n:
                    return
                t(already,i + 1)
                t(already | nums[i],i + 1)
        
        t(0,0)
        
        return ans