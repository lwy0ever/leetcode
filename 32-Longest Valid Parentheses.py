class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        n = len(s)
        # 从左到右扫描一次
        left = 0
        right = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    ans = max(ans,left + right)
                elif right > left:
                    left = 0
                    right = 0
        # 从右到左扫描一次
        left = 0
        right = 0
        for i in range(n - 1,-1,-1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
                if left == right:
                    ans = max(ans,left + right)
                elif right < left:
                    left = 0
                    right = 0
        
        return ans