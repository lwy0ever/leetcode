class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 二分查找
        n = len(intervals)
        for i,interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        ans = [-1] * n
        for _,end,ind in intervals:
            pos = bisect_left(intervals,[end])
            if pos < n:
                ans[ind] = intervals[pos][2]
        return ans
        
        # 双指针
        # 对start和end进行排序
        # ind指向第一个start
        # 逐个end处理
        # 如果这个end在start[ind]后面,则放弃该start,ind后移
        # 如果刚好在start[ind]前面,则这个start[ind]就是满足条件的右区间
        n = len(intervals)
        start,end = list(zip(*intervals))
        start = sorted(zip(start,range(n)))
        end = sorted(zip(end,range(n)))

        ans = [-1] * n
        ind = 0
        for e,i in end:
            while ind < n and start[ind][0] < e:
                ind += 1
            if ind < n:
                ans[i] = start[ind][1]
        return ans