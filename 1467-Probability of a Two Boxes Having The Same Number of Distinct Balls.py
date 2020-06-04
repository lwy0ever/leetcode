class Solution:
    def getProbability(self, balls: List[int]) -> float:
        # d[(a,b,c,d)]表示第1个袋子有a个球c种颜色,第2个袋子有b个球d种颜色的可能性
        d = {(0,0,0,0):1.0} # 初始化
        for i in range(len(balls)): # 逐个颜色进行尝试
            newD = collections.defaultdict(float)
            for k in d:
                for n in range(balls[i] + 1):   # 尝试每种分配方案
                    # 从balls[i]中取n个,方案数为C(balls[i],n)
                    # C(balls[i],n) = (math.factorial(balls[i]) / math.factorial(balls[i] - n)) / math.factorial(n)
                    # math.factorial(balls[i])为共有,可以忽略
                    newD[(k[0] + n,k[1] + balls[i] - n,k[2] + (1 if n > 0 else 0),k[3] + (1 if n < balls[i] else 0))] += d[k] / math.factorial(n) / math.factorial(balls[i] - n)
            d = newD
            #print(d)
        nn = 0
        good = 0
        for k in d:
            if k[0] == k[1]:
                nn += d[k]
                if k[2] == k[3]:
                    good += d[k]
        return good / nn