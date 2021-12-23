class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = collections.Counter(deliciousness)
        #print(cnt)
        twoS = [1]
        for _ in range(21): # 由于deliciousness[i]最大为2 ** 20,所以最大组合是2 ** 21
            twoS.append(twoS[-1] << 1)
        twoS = twoS[::-1]
        #print(twoS)
        ans = 0
        for k,v in cnt.items():
            for t in twoS:
                #print(k,v,t)
                if k > t - k:
                    break
                #print(k,t - k,(t - k) in cnt)
                if (t - k) in cnt:
                    if k < t - k:
                        ans += v * cnt[t - k]
                    else:   # k == t - k
                        ans += v * (v - 1) // 2
        return ans % (10 ** 9 + 7)