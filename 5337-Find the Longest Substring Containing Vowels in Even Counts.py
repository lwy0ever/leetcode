class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 用二进制记录出现的次数的奇偶性
        d = {'a':16,'e':8,'i':4,'o':2,'u':1}
        # 5个元音字母,所以有32种状态
        minPos = [float('inf')] * 32    # 各个状态首次出现的位置
        minPos[0] = -1  # 状态0首次出现的位置应该设定为-1(空字符串)
        maxPos = [-1] * 32  # 各个状态最后出现的位置
        stat = 0
        for i,c in enumerate(s):
            if c in d:
                stat ^= d[c]
            #print(c,pre)
            minPos[stat] = min(minPos[stat],i)
            maxPos[stat] = max(maxPos[stat],i)
        #print(minPos,maxPos)
        return max(maxPos[i] - minPos[i] for i in range(32))