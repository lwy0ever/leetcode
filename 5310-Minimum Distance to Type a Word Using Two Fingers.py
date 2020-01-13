class Solution:
    def minimumDistance(self, word: str) -> int:
        pos = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),
               (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),
               (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),
               (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),
               (4,0),(4,1)]
        base = ord('A')
        n = len(word)
        dp = {(i,j):0 for i in range(26) for j in range(26)}  # dp[(i,j)]表示手指A在字母i处,手指B在字母j处,需要的移动次数
        #print(dp)
        for c in word:
            newDP = {}
            for k in dp.keys():
                #print(k)
                # 移动A
                if (ord(c) - base,k[1]) not in newDP:
                    newDP[(ord(c) - base,k[1])] = dp[k] + abs(pos[ord(c) - base][0] - pos[k[0]][0]) + abs(pos[ord(c) - base][1] - pos[k[0]][1])
                else:
                    newDP[(ord(c) - base,k[1])] = min(newDP[(ord(c) - base,k[1])],dp[k] + abs(pos[ord(c) - base][0] - pos[k[0]][0]) + abs(pos[ord(c) - base][1] - pos[k[0]][1]))
                # 移动B
                if (k[0],ord(c) - base) not in newDP:
                    newDP[(k[0],ord(c) - base)] = dp[k] + abs(pos[ord(c) - base][0] - pos[k[1]][0]) + abs(pos[ord(c) - base][1] - pos[k[1]][1])
                else:
                    newDP[(k[0],ord(c) - base)] = min(newDP[(k[0],ord(c) - base)],dp[k] + abs(pos[ord(c) - base][0] - pos[k[1]][0]) + abs(pos[ord(c) - base][1] - pos[k[1]][1]))
            dp = newDP
        return min(dp.values())