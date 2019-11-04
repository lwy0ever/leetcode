class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        preEven = 0
        tailEven = 0
        oddNum = 0
        l = 0
        r = 0
        n = len(nums)
        while r < n:
            while r < n:
                r += 1
                if nums[r - 1] & 1 == 1:    # odd
                    oddNum += 1
                    if oddNum == k:
                        break
            if oddNum < k:
                break
            #print(preEven,l,r,oddNum,tailEven)
            tailEven = 0
            while r < n:
                if nums[r] & 1 == 0:
                    tailEven += 1
                    r += 1
                else:
                    break
            #print(preEven,l,r,oddNum,tailEven)
            preEven = 0
            while l < r:
                if nums[l] & 1 == 0:
                    preEven += 1
                    l += 1
                else:
                    ans += (preEven + 1) * (tailEven + 1)
                    oddNum -= 1
                    l += 1
                    break
            #print(preEven,l,r,oddNum,tailEven,ans)
        return ans
