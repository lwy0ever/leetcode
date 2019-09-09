class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 3:
            return ans
        nums.sort()
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                break
            j = i + 1
            k = n - 1
            while j < n - 1:
                if nums[i] + nums[j] > 0 and nums[j] > 0:
                    break        
                while k > j:
                    t = nums[i] + nums[j] + nums[k]
                    #print(i,j,k,t)
                    if t == 0:
                        ans.append([nums[i],nums[j],nums[k]])
                        while k - 1 > j and nums[k] == nums[k - 1]:
                            k -= 1
                        break
                    elif t < 0:
                        break
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                while j + 1 < n - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i + 1 < n - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans
                                    
                        
                    