class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 暴力模拟
        ans = []
        for s,e in zip(l,r):
            arr = sorted(nums[s:e + 1])
            if e - s <= 1:
                ans.append(True)
            else:
                step = (arr[-1] - arr[0]) / (e - s)
                for i in range(1,e - s):
                    if arr[i] != arr[0] + step * i:
                        ans.append(False)
                        break
                else:
                    ans.append(True)
        return ans
                    