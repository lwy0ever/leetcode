class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # 找素数
        # 由于1 <= nums[i] <= 30
        # 1到30的素数有:2,3,5,7,11,13,17,19,23,29
        # 1比较特殊,可以无限次使用
        primes = [2,3,5,7,11,13,17,19,23,29]
        m = 10 ** 9 + 7
        cnt = collections.Counter(nums)

        status = [0] * (1 << len(primes))
        status[0] = 2 ** cnt[1] % m # 1可以贡献的次数
        
        for k,v in cnt.items():
            if k == 1:
                continue
                
            # 检查k的因子情况
            kStatus = 0
            for j,p in enumerate(primes):
                if k % (p * p) == 0:    # p出现2次或以上,直接放弃
                    break
                if k % p == 0:  # p出现1次,记录
                    kStatus |= (1 << j)
            else:   # 没有出现2次及以上p的情况
                for mask in range((1 << len(primes)) - 1,0,-1):    # 倒着检查
                    if mask & kStatus == kStatus:  # 有效的s
                        # 有1种方案:从mask到mask
                        # 还有v种方案:从mask ^ kStatus到mask
                        status[mask] = (status[mask] + status[mask ^ kStatus] * v) % m
        return sum(status[1:]) % m