class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        s = 0
        # 计算每个任务浪费的能量,尽可能少浪费
        tasks.sort(key = lambda x:x[1] - x[0])
        ans = tasks[0][1] - tasks[0][0]
        for t in tasks:
            #print(ans,t)
            if ans < t[1] - t[0]:
                ans = t[1] - t[0]
            ans += t[0]
            #print(ans)
        return ans