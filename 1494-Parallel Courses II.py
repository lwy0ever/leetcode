class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 类贪心算法是错误的
        # 如下测试用例:
        # 12
        # [[1,2],[2,3],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12]]
        # 3
        # 答案应该是4,而不是5
        
        # dp + 状态压缩
        # 尝试在第term个学期,学习courseCanLearn中的课程
        # 本次尝试courseCanLearn[ind]
        # courseCanLearn的长度为m
        # 最多还可以学习limit门课程
        # 当前学过课程的状态是status
        def dfs(ind,m,limit,term,status):
            if m - ind < limit: # 剩下可学的课程数量低于限制值,一定有可以学的课程错过了,不是最优解
                return
            if limit == 0 or ind == m:  # 达到可以学习的课程上限or没有可以尝试的课程了
                if dp[status] == -1 or dp[status] > term:   # 出现了新的,更好的解决方案
                    dp[status] = term
            else:
                # 学习courseCanLearn[ind]
                dfs(ind + 1,m,limit - 1,term,status | (1 << courseCanLearn[ind]))
                # 不学习courseCanLearn[ind]
                dfs(ind + 1,m,limit,term,status)
        # dp[i]表示学完bin(i)的课程需要的学期数(默认-1)
        # 其中i为状态压缩值,例如i = 11001,表示学习课程5,4,1
        dp = [-1] * (1 << n)
        dp[0] = 0   # 学习0课程,需要0学期
        preCourse = [0] * n # preCourse[i]表示学习课程i所需要的直接前导课程
        for pre,c in dependencies:
            preCourse[c - 1] |= 1 << (pre - 1)
        #print(preCourse)
        for i in range(1 << n): # 对逐个状态i进行遍历
            if dp[i] == -1: # 该状态从未出现过,跳过
                continue
            courseCanLearn = [] # 可以学习的课程
            for j in range(n):
                if i & (1 << j):    # 这个课程已经学习过
                    continue
                if preCourse[j] & i != preCourse[j]:    # 这个课程的前导课程还没有学完
                    continue
                courseCanLearn.append(j)    # 该课程可以学习
            m = len(courseCanLearn)
            # 尝试在第dp[i] + 1个学期,学习courseCanLearn中的课程
            # 本次尝试courseCanLearn[0]
            # courseCanLearn的长度为m
            # 最多还可以学习min(m,k)门课程
            # 当前学过课程的状态是i
            dfs(0,m,min(m,k),dp[i] + 1,i)
        #print(dp)
        return dp[-1]