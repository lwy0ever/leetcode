class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            preAns = ans
            preChar = ''
            cnt = 0
            ans = []
            for c in preAns:
                if c == preChar:
                    cnt += 1
                else:
                    if cnt > 0:
                        ans.append(str(cnt) + preChar)
                    preChar = c
                    cnt = 1
            ans.append(str(cnt) + c)
            ans = ''.join(ans)
            #print(ans)
        return ans