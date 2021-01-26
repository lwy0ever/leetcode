class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        age_score = list(zip(ages,scores))
        # 按年龄升序,年龄相同按照得分升序
        age_score.sort(key = lambda x:(x[0],x[1]))
        # dp[i]表示包含age_score[i]的情况下的最高得分
        dp = [x[1] for x in age_score]
        for last in range(n):
            for i in range(last):
                # 由于已经按照age排序,只要score满足,则必然满足
                # 由于age_score[i]被选中,所以dp[i]的方案里面,一定没有大于age_score[i][1]的
                if age_score[last][1] >= age_score[i][1]:
                    dp[last] = max(dp[last],dp[i] + age_score[last][1])
        return max(dp)