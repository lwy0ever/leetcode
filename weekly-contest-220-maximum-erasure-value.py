class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 双指针
        n = len(nums)
        ans = 0
        appeared = set()
        s = 0
        left = 0
        right = 0
        while right < n:
            if nums[right] in appeared:
                while True:
                    s -= nums[left]
                    appeared.remove(nums[left])
                    left += 1
                    if nums[left - 1] == nums[right]:
                        break
            s += nums[right]
            ans = max(ans,s)
            appeared.add(nums[right])
            right += 1
            #print(left,right,s,appeared)
        return ans
