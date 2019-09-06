class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_profit = list(zip(difficulty, profit))
        diff_profit.sort()
        ans = pos = ma_pro = 0
        for skill in sorted(worker):
            while pos < len(diff_profit) and skill >= diff_profit[pos][0]:
                ma_pro = max(ma_pro, diff_profit[pos][1])
                pos += 1
            ans += ma_pro
        return ans
        '''
        diff_profit = list(zip(difficulty,profit))
        diff_profit.sort(key = lambda x : x[0])
        #print(diff_profit)
        diff,prof = zip(*diff_profit)
        #print(diff,prof)
        ma_pro = [0]
        for p in prof:
            ma_pro.append(max(ma_pro[-1],p))
        ans = 0
        for w in worker:
            pos = bisect.bisect_right(diff,w)
            ans += ma_pro[pos]
        return ans
        '''        