class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subtotal,m = divmod(sum(nums),k)
        if m > 0:
            return False
        nums.sort(reverse = True)
        used = set()
        n = len(nums)
        if nums[0] > subtotal:
            return False
        
        def dfs(i,start,tmp):   #在凑第i个subsets,从nums的第start个开始,当前已经凑了tmp了
            if tmp == subtotal:
                return dfs(i + 1,0,0)
            if i == k - 1:  #subsets[0]...subsets[k-2]已经ok,则subsets[k-1]自然ok
                return True
            for j in range(start,n):
                if j not in used:
                    if tmp + nums[j] <= subtotal:
                        used.add(j) #尝试将j加入
                        if dfs(i,j + 1,tmp + nums[j]):
                            return True
                        used.remove(j)  #加入j失败,移除
            return False
        
        return dfs(0,0,0)
