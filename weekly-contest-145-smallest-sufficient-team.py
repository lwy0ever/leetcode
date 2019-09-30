class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sn = len(req_skills)
        # 技能-技能顺序号映射
        skill_index = {}
        for i in range(sn):
            skill_index[req_skills[i]] = i
        #full = 1 << sn - 1
        # 人员技能情况，二进制表示
        pp = []
        for p in people:
            ps = 0
            for sk in p:
                ps |= 1 << skill_index[sk]
            pp.append(ps)
        #print(pp)
        
        pn = len(people)
        # 表示people的加入情况
        # dp[i] 表示构成技能i所需要的人员情况，默认需要所有人
        dp = [list(range(pn)) for _ in range(1 << sn)]
        dp[0] = []
        for i in range(pn):
            if pp[i] == 0:
                continue
            for k, v in enumerate(dp):
                # 把这个人p加入进来以后的团队技能情况
                new_skills = k | pp[i]
                # 如果团队技能因此而增加,并且增加后的人数比新技能原来的人数少,则更新答案
                if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                    dp[new_skills] = v + [i]

        return dp[-1]