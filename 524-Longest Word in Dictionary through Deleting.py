class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 方法2:
        # 在s中查找字符的时候,做预处理,这样就不需要逐个字符查找
        m = len(s)
        dp = [[0] * 26 for _ in range(m + 1)]   # dp[i][j]表示从s[i]开始,下一个字符chr(97 + j)出现的位置(s只含小写字母)
        # 预处理
        dp[m] = [m] * 26    # m - 1后面没有字符
        for i in range(m - 1,-1,-1):
            for j in range(26):
                if ord(s[i]) - 97 == j:
                    dp[i][j] = i    # i是下一个出现的位置
                else:
                    dp[i][j] = dp[i + 1][j] # i + 1是下一个出现的位置
        ans = ''
        for d in dictionary:
            matched = True
            i = 0
            for j in range(len(d)):
                if dp[i][ord(d[j]) - 97] == m:  # 无法匹配
                    matched = False
                    break
                else:
                    i = dp[i][ord(d[j]) - 97] + 1
            if matched:
                if len(d) > len(ans) or (len(d) == len(ans) and d < ans):
                    ans = d
        return ans
        
        # 方法1:
        # 最基本思路,逐个比对
        ans = ''
        n = len(s)
        for d in dictionary:
            ind = 0
            iS = 0
            ld = len(d)
            while iS < n and ind < ld:
                if s[iS] == d[ind]: # 多匹配了一个
                    ind += 1
                iS += 1
            if ind == ld:   # 全部匹配
                if len(d) > len(ans) or (len(d) == len(ans) and d < ans):
                    ans = d
        return ans