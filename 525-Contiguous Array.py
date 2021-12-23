class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        # pos[i]中的i,表示1比0多出现的次数
        # i=0,表示0和1数量相等
        # i>0,表示1比0多
        # i<0,表示1比0少
        # pos[i]表示这种情况最早出现的位置
        pos = dict()
        pos[0] = -1
        cnt = 0
        for i,n in enumerate(nums):
            if n == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt in pos:
                ans = max(ans,i - pos[cnt])
            else:
                pos[cnt] = i
            #print(i,cnt,ans,pos)
        return ans