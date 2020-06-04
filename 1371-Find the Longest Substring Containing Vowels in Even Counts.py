class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 用二进制xxxxx表示元音出现的次数
        # 出现偶数次用0表示,出现奇数次用1表示
        d = {'a':1,'e':2,'i':4,'o':8,'u':16}
        n = len(s)
        minPos = [n] * (2 ** 5) # minPos[i]表示状态i出现的最小位置
        maxPos = [-1] * (2 ** 5) # maxPos[i]表示状态i出现的最大位置
        minPos[0] = -1  # 状态0首次出现的位置应该设定为-1(空字符串)
        status = 0
        for i in range(n):
            if s[i] in d:
                status ^= d[s[i]]
            minPos[status] = min(minPos[status],i)
            maxPos[status] = i
        #print(minPos)
        #print(maxPos)
        ans = 0
        for x in range(2 ** 5):
            ans = max(ans,maxPos[x] - minPos[x])
        return ans