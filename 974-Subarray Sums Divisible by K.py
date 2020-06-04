class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cnt = [0] * K   # cnt[i]表示A[:x]的和余数是i的个数
        cnt[0] = 1  # 余数是0的情况下,可以自治
        s = 0
        for x in A:
            s = (s + x) % K
            cnt[s] += 1
        ans = 0
        for c in cnt:
            ans += c * (c - 1) // 2
        return ans