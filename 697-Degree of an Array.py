class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()  # d[x] = [cnt,start,end],表示nums中的元素x出现的频次cnt,开始位置start,结束位置end
        for i,n in enumerate(nums):
            if n in d:
                d[n][2] = i
                d[n][0] += 1
            else:
                d[n] = [1,i,i]
        #print(d)
        ans = 0
        maxCnt = 0
        for cnt,s,e in d.values():
            if cnt > maxCnt:
                maxCnt = cnt
                ans = e - s + 1
            elif cnt == maxCnt:
                ans = min(ans,e - s + 1)
        return ans