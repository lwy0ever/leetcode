class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        n = len(nums)
        nums.sort()
        #print(nums)
        i = 0
        while i < n - 2:
            j = i + 1
            k = n - 1
            while j < n - 1:
                while k > j:
                    t = nums[i] + nums[j] + nums[k]
                    #print(i,j,k,t)
                    if t == target:
                        return t
                    elif t > target:
                        if t - target < abs(ans - target):
                            ans = t
                    else:   # t < target
                        if target - t < abs(target - ans):
                            ans = t
                        break
                    k -= 1
                j += 1
            i += 1
        return ans                