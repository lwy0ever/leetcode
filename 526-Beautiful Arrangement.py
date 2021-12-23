class Solution:
    def countArrangement(self, n: int) -> int:
        # 状态再压缩
        stat = collections.defaultdict(int)
        stat[0] = 1
        for num in range(1,n + 1):
            new_stat = collections.defaultdict(int)
            for i in range(1,n + 1):
                for k in stat.keys():
                    if k & (1 << (i - 1)) == 0 and (i % num == 0 or num % i == 0):
                        new_stat[k | (1 << (i - 1))] += stat[k]
            stat = new_stat
            #print(stat)
        return stat[(1 << n) - 1]
    
        '''
        # 状态压缩
        stat = [0] * (1 << n)  # stat[mask]表示状态为mask的方案数量
        stat[0] = 1
        for mask in range(1,1 << n):
            num = bin(mask).count('1')  # 当前状态mask已经放置了多少个数字
            for i in range(1,n + 1):
                if mask & (1 << (i - 1)) and (i % num == 0 or num % i == 0):
                    stat[mask] += stat[mask ^ (1 << (i - 1))]
        #print(stat)
        return stat[(1 << n) - 1]
        '''