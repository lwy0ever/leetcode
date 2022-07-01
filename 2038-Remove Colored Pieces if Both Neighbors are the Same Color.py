class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Alice和Bob的操作相互独立
        # 分别统计Alice和Bob可以操作的次数
        # 如果Alice > Bob,Alice胜
        # 否则Bob胜
        pre = ''
        cnt = 0
        AB = {'A':0,'B':0}
        for c in colors:
            #print('from',pre,cnt,AB)
            if c == pre:
                cnt += 1
            else:
                if cnt >= 3:
                    AB[pre] += cnt - 2
                pre = c
                cnt = 1
            #print('to',pre,cnt,AB)
        if cnt >= 3:
            AB[c] += cnt - 2
        #print(AB)
        return True if AB['A'] > AB['B'] else False