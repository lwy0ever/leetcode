class Solution:
    def numWays(self, s: str) -> int:
        cnt = collections.Counter(s)
        if cnt['1'] == 0:
            return (cnt['0'] - 1 - 1 + 1) * (cnt['0'] - 1 - 1) // 2 % (10 ** 9 + 7)
        if cnt['1'] % 3 != 0:
            return 0
        t = cnt['1'] // 3
        # 每个子字符串需要t个1
        # 刚刚有t个1时,记录位置为start,最长可以到达的位置,记录为end
        ct = 0
        start = 0
        end = 0
        pos = []
        for i,c in enumerate(s):
            if c == '1':
                ct += 1
                if ct == t + 1:
                    end = i
                    pos.append([start,end])
                    ct = 1
                if ct == t:
                    start = i
            #print(i,c,ct,start,end)
        #print(pos)
        return (pos[0][1] - pos[0][0]) * (pos[1][1] - pos[1][0]) % (10 ** 9 + 7)