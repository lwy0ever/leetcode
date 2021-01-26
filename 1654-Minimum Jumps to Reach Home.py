class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        # bfs
        forbidden = set(forbidden)
        fromP = [(0,True)]  # (p,bool):p表示所在位置,bool表示是否可以后跳
        ans = 0
        if a >= b:  # 如果a >= b,那么f + a最远到达x + b,再远就不可能回来了
            maxP = x + b
        else:
            maxP = x + b + a * b // math.gcd(a, b)
        while fromP:
            ans += 1
            toP = []
            for f,canBack in fromP:
                if f + a == x:
                    return ans
                if f + a not in forbidden and f + a <= maxP:
                    toP.append((f + a,True))
                    forbidden.add(f + a)    # 由于前跳经过点f + a,从f + a可以前跳,也可以后跳,所以f + a不需要再考虑
                if canBack and f - b > 0 and f - b not in forbidden:
                    if f - b == x:
                        return ans
                    toP.append((f - b,False))
                    # 由于后跳经过点f - b,从f - b只能前跳,不能后跳,所以f - b还有再考虑的必要
                    #forbidden.add(f - b)
            fromP = toP
            #print(fromP)
        return -1