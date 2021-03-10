class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        s = sum(A)
        if s % 3 != 0:
            return False
        avg = s // 3
        cl = 0
        cr = n - 1
        l = 0
        r = 0
        while cl < cr:
            #print(cl,cr,l,r)
            if l != avg:
                l += A[cl]
                cl += 1
            if r != avg:
                r += A[cr]
                cr -= 1
            if l == avg and r == avg:
                return True
        return False
        '''
        presum = [A[0]]
        n = len(A)
        if n < 3:
            return False
        for i in range(1,n):
            presum.append(presum[i - 1] + A[i])
        #print(presum)
        if presum[-1] % 3 != 0:
            return False
        ms = [presum[-1] // 3 * 2,presum[-1] // 3]
        m = ms.pop()
        for i in range(0,n - 1):
            if m == presum[i]:
                #print(m,i)
                if ms:
                    m = ms.pop()
                else:
                    return True
        return False
        '''