class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j]表示s的前i个字符 和 p的前j个字符是否匹配
        # 初始化:
        # dp[0][0]:什么都没有,所以为true
        # 第一行dp[0][j],换句话说,s为空,与p匹配,所以只要p开始为*才为true
        # 第一列dp[i][0],当然全部为False
        # 动态方程:
        # 如果(s[i] == p[j] or p[j] == "?") and dp[i-1][j-1] ,有dp[i][j] = true
        # 如果p[j] == "*" and (dp[i-1][j] == true or dp[i][j-1] == true) 有dp[i][j] = true
        # note:
        # dp[i][j-1],表示*代表是空字符,例如ab,ab*
        # dp[i-1][j],表示*代表非空任何字符,例如abcd,ab*
        sn = len(s)
        pn = len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        
        # dp[0][j],也就是说,s为空,如果要与p匹配,要p开始为*才为true
        for j in range(1,pn + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
                
        for i in range(1,sn + 1):
            for j in range(1,pn + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # dp[i][j] = dp[i][j - 1] 意味着 * 代表空字符
                    # dp[i][j] = dp[i - 1][j] 意味着 * 代表非空字符
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[sn][pn]
