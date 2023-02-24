class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subtotal,m = divmod(sum(nums),k)
        if m > 0:
            return False
        nums.sort()
        n = len(nums)
        if nums[-1] > subtotal:
            return False
        
        @cache
        def dfs(s,tmp): # s表示已使用情况(1表示未使用,0表示已使用),当前已经凑了tmp了
            if s == 0:
                return True
            for i in range(n):
                if tmp + nums[i] > subtotal:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i),(tmp + nums[i]) % subtotal):
                    return True
            return False
        
        return dfs((1 << n) - 1,0)