class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 统计[s1,n1]中包括的s2的数量cnt
        # 则答案就是cnt // n2
        # tips:
        # 在统计cnt的时候,记录匹配一个s1之后,s2的位置
        # 当s2的位置出现重复的时候,说明出现了循环
        l1 = len(s1)
        l2 = len(s2)
        pos2 = dict()   # pos2[p] = (s1cnt,s2cnt),表示经过s1cnt个s1之后,s2的位置p,并且匹配成功了s2cnt个s2
        s1cnt = 0
        s2cnt = 0
        p = 0
        while True:
            for c1 in s1:
                if c1 == s2[p]: # 有一个匹配的
                    p += 1
                    if p == l2: # s2匹配完毕,从0开始
                        p = 0
                        s2cnt += 1
            s1cnt += 1
            if s1cnt == n1:
                return s2cnt // n2  # 还没有出现循环(或者刚刚出现循环,还没有进入判断循环的阶段)就已经到了n1
            if p in pos2:   # 出现了循环
                s1pre,s2pre = pos2[p]
                s1loop,s2loop = s1cnt - s1pre,s2cnt - s2pre
                break
            else:
                pos2[p] = (s1cnt,s2cnt)
        #print(s1loop,s2loop,s1pre,s2pre)
        cnt = s2pre + (n1 - s1pre) // s1loop * s2loop
        #print(cnt)
        # 剩余部分,暴力统计
        s2cnt = 0
        rest = (n1 - s1pre) % s1loop
        #print(rest,p)
        for i in range(rest):
            for c1 in s1:
                if c1 == s2[p]:
                    p += 1
                    if p == l2:
                        p = 0
                        s2cnt += 1
        #print(cnt,s2cnt)
        return (cnt + s2cnt) // n2