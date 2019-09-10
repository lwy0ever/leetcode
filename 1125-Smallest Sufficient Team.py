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
        
        sk_num = {}
        def cnt(x):
            nonlocal sk_num
            #print(sk_num)
            if x in sk_num:
                return sk_num[x]
            t = x
            r = 0
            while x > 0:
                x &= x - 1
                r += 1
            sk_num[t] = r
            return r

        pn = len(people)
        # 表示people的加入情况
        # dp[i] 表示构成技能i所需要的人员情况，默认需要所有人
        dp = [list(range(pn)) for _ in range(1 << sn)]
        #dp = [(1 << pn) - 1] * (1 << sn)
        dp[0] = []
        #dp[0] = 0
        for k, v in enumerate(dp):
            for i in range(pn):
                if not pp[i]:
                    continue
                # 把这个人p加入进来以后的团队技能情况
                new_skills = k | pp[i]
                # 如果团队技能因此而增加,并且增加后的人数比新技能原来的人数少,则更新答案
                if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                    dp[new_skills] = v + [i]
                #if new_skills != k and cnt(dp[new_skills]) > cnt(v) + 1:
                #    dp[new_skills] = v | (1 << i)
                #print(k,v,i,pp[i],new_skills,k,cnt(dp[new_skills]),cnt(v),dp)

        '''
        ans = []
        i = 0
        x = dp[-1]
        while x > 0:
            if x & 1:
                ans.append(i)
            i += 1
            x >>= 1
        return ans
        '''
        return dp[-1]