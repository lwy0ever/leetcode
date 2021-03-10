class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 借助一个标志列表status,用于判断每个节点i(课程)的状态:
        # 未被 DFS 访问:status[i] = 0
        # 已被其他节点启动的DFS访问:i = -1
        # 已被当前节点启动的DFS访问:i = 1
        def dfs(c):
            if status[c] == -1:
                return True
            if status[c] == 1:
                return False
            status[c] = 1
            for pre in d[c]:
                if not dfs(pre):
                    return False
            status[c] = -1
            return True

        d = collections.defaultdict(list)
        #isGoodCourse = [False] * numCourses
        status = [0] * numCourses
        for course,pre in prerequisites:
            d[course].append(pre)
        for i in range(numCourses):
            # check circle
            # dfs
            if not dfs(i):
                return False
        return True