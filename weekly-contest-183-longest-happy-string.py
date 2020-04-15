class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 选择最多的字符串,并记录最后添加的字符串
        d = {'a':a,'b':b,'c':c}
        ans = []
        while True:
            t = sorted([(k,v) for k,v in d.items()],key = lambda x:x[1],reverse = True)
            if t[0][1] == 0:
                break
            if len(ans) < 2:
                ans.append(t[0][0])
                d[t[0][0]] -= 1
            else:
                if t[0][0] == ans[-1] and t[0][0] == ans[-2]:
                    if t[1][1] == 0:
                        break
                    else:
                        ans.append(t[1][0])
                        d[t[1][0]] -= 1
                else:
                    ans.append(t[0][0])
                    d[t[0][0]] -= 1
        return ''.join(ans)