class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # XL -> LX,也就是L左侧遇到X可以左移
        # RX -> XR,也就是R右侧遇到X可以右移
        # L和R不能相互跨越
        n = len(start)
        Ls = 0  # 表示end积压的L的需求
        Rs = 0  # 表示start积压的R的能力
        for i in range(n):
            if start[i] == end[i]:
                if end[i] == 'L' and Rs > 0 or start[i] == 'R' and Ls > 0:
                    return False
                continue
            if end[i] == 'L':   # 需要L
                if Rs > 0 or start[i] == 'R':
                    return False
                else:
                    Ls += 1
            elif end[i] == 'R': # 需要R
                if Ls > 0 or start[i] == 'L':
                    return False
                else:   # X
                    if Rs > 0:
                        Rs -= 1
                    else:
                        return False
            else:   # end[i] == X
                if start[i] == 'L':
                    if Ls > 0:
                        Ls -= 1
                    else:
                        return False
                else:   # R
                    Rs += 1
            #print(Ls,Rs)
        return Ls == Rs == 0