class Solution:
    def maxDepth(self, s: str) -> int:
        # 直接统计最深的括号
        ans = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
                ans = max(ans,cnt)
            elif c == ')':
                cnt -= 1
        return ans

        # 拆分成VPS,然后递归统计嵌套深度
        '''
        ans = 0
        n = len(s)
        start = 0
        cnt = 0
        for i in range(n):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            if cnt == 0:
                if i == start:
                    ans = max(ans,0)
                else:
                    ans = max(ans,1 + self.maxDepth(s[start + 1:i]))
                start = i + 1
        #print(s,ans)
        return ans
        '''