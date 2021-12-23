class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 二分法 + 回溯

        # 分配jobs,已经分配的为workers,最大分配limit
        def dfs(jobs, workers, limit):  # workers[i]代表第i个工人所用的时间
            if not jobs:
                return True # jobs为空说明工作都分完了,可以在limit时间内由k名工人完成所有工作
            v = jobs.pop()
            for i, w in enumerate(workers):
                if w + v <= limit:
                    workers[i] += v
                    if dfs(jobs, workers, limit):
                        return True
                    workers[i] -= v
                if w == 0: # 剪枝:该worker未被分配job,说明其后的worker也没有被分配job,不需要再考虑其后的worker
                    break
            jobs.append(v)
            return False

        jobs.sort()
        l,r = jobs[-1],sum(jobs)
        while l < r:
            mid = l + (r - l) // 2
            if dfs(jobs[:], [0] * k, mid):
                r = mid
            else:
                l = mid + 1
        return l