class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ans = [0]
        if k < 0:
            for i in range(k,0):
                ans[0] += code[i]
        else:
            for i in range(1,k + 1):
                ans[0] += code[i % n]
        #print(ans)
        for i in range(1,n):
            if k < 0:
                ans.append(ans[-1] - code[(i + k - 1) % n] + code[(i - 1) % n])
            else:
                ans.append(ans[-1] - code[i] + code[(i + k) % n])
        return ans