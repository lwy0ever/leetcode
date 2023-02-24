class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # 使p[0]和p[1]的最低位不同
        # p[0:2]反转之后,使第2位不同,形成p[2:4]
        # p[0:4]反转之后,使第3位不同,形成p[4:8]
        # ...
        ans = [start]
        for i in range(n):
            for j in range(2 ** i - 1,-1,-1):
                ans.append(ans[j] ^ (2 ** i))
        #print(list(map(bin,ans)))
        return ans