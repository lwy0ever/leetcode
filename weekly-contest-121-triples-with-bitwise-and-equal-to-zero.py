class Solution:
    def countTriplets(self, A: List[int]) -> int:
        # 方法1:标记
        cache = [0] * (1 << 16) # cache[i]表示可以和i按位与成0的数字的数量
        mask = (1 << 16) - 1
        for a in A:
            canZero = mask ^ a  # 表示可以和a形成0的所有1的位置
            oneS = canZero
            while oneS:
                cache[oneS] += 1
                # 这步很精妙
                oneS = (oneS - 1) & canZero
            cache[0] += 1
        ans = 0
        for a in A:
            for b in A:
                ans += cache[a & b]
        return ans
        '''
        # 方法2:字典缓存
        preCal = collections.defaultdict(int)    # preCal[i]表示A[i] & A[j] == i的组合数量
        n = len(A)
        for i in range(n):
            for j in range(n):
                preCal[A[i] & A[j]] += 1
        ans = 0
        for i in range(n):
            for k in preCal.keys():
                if A[i] & k == 0:
                    ans += preCal[k]
        return ans
        '''