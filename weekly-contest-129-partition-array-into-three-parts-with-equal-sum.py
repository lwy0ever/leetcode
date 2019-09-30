class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        presum = [A[0]]
        n = len(A)
        if n < 3:
            return False
        for i in range(1,n):
            presum.append(presum[i - 1] + A[i])
        print(presum)
        if presum[-1] % 3 != 0:
            return False
        ms = [presum[-1] // 3 * 2,presum[-1] // 3]
        m = ms.pop()
        for i in range(0,n - 1):
            if m == presum[i]:
                print(m,i)
                if ms:
                    m = ms.pop()
                else:
                    return True
        return False
            