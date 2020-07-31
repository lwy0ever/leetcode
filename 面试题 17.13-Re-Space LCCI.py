class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dp = [0] * (n + 1)  # dp[i]表示sentence[:i]的未识别字符数
        dic = set(dictionary)
        lens = set()    # 存储所有可能的长度,这样就不需要再关注无效的长度
        for d in dic:
            lens.add(len(d))
        lens = sorted(list(lens))
        for i in range(1,n + 1):
            dp[i] = dp[i - 1] + 1
            for l in lens:
                if i - l >= 0:
                    if sentence[i - l:i] in dic:
                        dp[i] = min(dp[i],dp[i - l])
                else:
                    break
        return dp[-1]