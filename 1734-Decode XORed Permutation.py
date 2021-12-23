class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # e[i] = p[i] ^ p[i + 1]
        
        # e[0] ^ ... ^ e[n - 2]
        # = p[0] ^ p[1] ^ p[1] ^ p[2] ^ ... ^ p[n - 2] ^ p[n - 1]
        # = p[0] ^ p[n - 1]

        # encoded一共有n - 1个(偶数个)
        # eA
        # = e[0] ^ e[2]  ^ e[4] ^ ... ^ e[n - 3]
        # = p[0] ^ p[1] ^ p[2] ^ p[3] ^ ... ^ p[n - 2]

        # eB
        # = e[1] ^ e[3]  ^ e[5] ^ ... ^ e[n - 2]
        # = p[1] ^ p[2] ^ p[3] ^ p[4] ^ ... ^ p[n - 1]
        
        # 定义X = p[0] ^ ... ^ p[n - 1]
        # 那么X ^ eB = p[0]
        
        # 有了p[0]之后
        # p[1] = e[0] ^ p[0]
        # p[2] = e[1] ^ p[1]
        
        n = len(encoded) + 1
        X = reduce(xor,range(1,n + 1))
        eB = 0
        for i in range(1,n - 1,2):
            eB ^= encoded[i]
        ans = []
        ans.append(X ^ eB)
        for i in range(n - 1):
            ans.append(ans[-1] ^ encoded[i])
        return ans