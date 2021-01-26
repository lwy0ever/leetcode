class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnt = collections.Counter(nums) # 表示每个数字出现的次数
        cnt = sorted(cnt.values())   # 可以选择的次数列表
        #print(cnt)
        quantity.sort(reverse = True)
        
        cache = dict()
        def d(cnt,i):   # 考虑排序后的第i个顾客,当前可以选择的次数列表是cnt
            if i == len(quantity):
                return True
            if (cnt,i) in cache:
                return cache[(cnt,i)]
            lastChoice = -1 # 上次选择的次数
            n = len(cnt)
            for c in range(n - 1,-1,-1):
                if cnt[c] < quantity[i]:
                    break
                if cnt[c] != lastChoice:
                    lastChoice = cnt[c]
                    new_cnt = list(cnt)
                    if cnt[c] - quantity[i] > 0:
                        new_cnt[c] = lastChoice - quantity[i]
                        new_cnt.sort()
                    else:
                        new_cnt.pop(c)
                    if d(tuple(new_cnt),i + 1):
                        cache[(cnt,i)] = True
                        return True
                else:
                    continue
            cache[(cnt,i)] = False
            return False
        
        # 先考虑大数,后考虑小数,有利于控制规模
        return d(tuple(cnt),0)