class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = collections.Counter(t)
        ans = ''
        r = 0
        n = len(s)
        ansL = 0
        ansR = n + 1
        ansMinLen = n + 1
        stack = []    # 存储在t里面的元素的位置
        stackIndex = 0
        while r < n:
            if s[r] in cnt:
                cnt[s[r]] -= 1
                stack.append(r)
                r += 1
            else:
                r += 1
                continue
            #print(stack,stackIndex,s[stack[stackIndex]],r,cnt,+cnt)
            # 还有未满足的
            if len(+cnt) > 0:
                continue
            # 都满足了
            while len(+cnt) == 0:
                if ansMinLen > r - stack[stackIndex]:
                    ansL = stack[stackIndex]
                    ansR = r
                    ansMinLen = ansR - ansL
                cnt[s[stack[stackIndex]]] += 1
                stackIndex += 1
                #print(stack,stackIndex,cnt)
        return s[ansL:ansR] if ansR - ansL <= n else ''