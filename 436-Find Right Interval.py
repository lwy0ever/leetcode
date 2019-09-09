from collections import defaultdict
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        leftPos = {}
        rightPos = defaultdict(list)
        n = len(intervals)
        for i in range(n):
            leftPos[intervals[i][0]] = i
            rightPos[intervals[i][1]].append(i)
        '''
        rightPosMinleft = {}  # right:(pos,Minleft)
        rightPoss = defaultdict(list)
        n = len(intervals)
        for i in range(n):
            if intervals[i][1] in rightPosMinleft:
                if rightPosMinleft[intervals[i][1]][1] > intervals[i][1] - intervals[i][0]:
                    rightPosMinleft[intervals[i][1]] = (i,intervals[i][1] - intervals[i][0])
            else:
                rightPosMinleft[intervals[i][1]] = (i,intervals[i][1] - intervals[i][0])
            rightPoss[intervals[i][1]].append(i)
        '''
        ans = [-1] * n
        left = sorted(leftPos.keys())
        right = sorted(rightPos.keys())
        l = 0
        r = 0
        while l < n and r < n:
            if right[r] <= left[l]:
                for p in rightPos[right[r]]:
                    ans[p]= leftPos[left[l]]
                r += 1
            else:
                l += 1
        return ans