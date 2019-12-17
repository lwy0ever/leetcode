class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 借助一个标志列表status,用于判断每个节点i(课程)的状态:
        # 未被 DFS 访问:status[i] = 0
        # 已被其他节点启动的DFS访问:i = -1
        # 已被当前节点启动的DFS访问:i = 1
        status = [0] * numCourses
        ans = []
        
        def dfs(c):
            #print(c,status[c])
            ans = []    # 记录当前课程及其前置课程,存储顺序:课程->前置课程
            if status[c] == -1:
                return True,ans
            if status[c] == 1:
                return False,ans
            # 当status[c] = 0的情况
            status[c] = 1
            for p in pre[c]:
                isCir,arr = dfs(p)
                if not isCir:
                    return False,[]
                ans = arr + ans    # 由于ans已有的课程可能是arr的前置课程,所以需要用arr + ans,而不是ans + arr
            status[c] = -1
            ans.insert(0,c) # 加入当前课程
            #print(c,ans)
            return True,ans
        
        pre = collections.defaultdict(list)
        for c,p in prerequisites:
            pre[c].append(p)
        #print(pre)
        for i in range(numCourses):
            isCir,arr = dfs(i)
            if not isCir:
                return []
            ans = arr + ans # 由于ans已有的课程可能是arr的前置课程,所以需要用arr + ans,而不是ans + arr
        return ans[::-1]