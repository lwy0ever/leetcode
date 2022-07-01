class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 选择最多的字符串,并记录最后添加的字符串
        d = [['a',a],['b',b],['c',c]]
        ans = []
        while True:
            d.sort(key = lambda x:-x[1])
            if d[0][1] == 0:
                break
            if len(ans) < 2:
                ans.append(d[0][0])
                d[0][1] -= 1
            else:
                if d[0][0] == ans[-1] and d[0][0] == ans[-2]:
                    if d[1][1] == 0:
                        break
                    else:
                        ans.append(d[1][0])
                        d[1][1] -= 1
                else:
                    ans.append(d[0][0])
                    d[0][1] -= 1
        return ''.join(ans)