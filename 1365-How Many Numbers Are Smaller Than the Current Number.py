class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 方法1:利用 0 <= nums[i] <= 100
        cnt = [0] * 101 # 记录每个nums[i]出现的次数
        for n in nums:
            cnt[n] += 1
        for i in range(99):
            cnt[i + 1] += cnt[i]
        ans = []
        for n in nums:
            ans.append(cnt[n - 1] if n > 0 else 0)
        return ans
        # 方法2:排序
        '''
        n = len(nums)
        ans = [0] * n
        arr = list(zip(nums,range(n)))
        arr.sort()
        #print(arr)
        for i in range(1,n):
            if arr[i][0] > arr[i - 1][0]:
                ans[arr[i][1]] = i
            else:   # arr[i][0] == arr[i - 1][0]
                ans[arr[i][1]] = ans[arr[i - 1][1]]
        return ans
        '''