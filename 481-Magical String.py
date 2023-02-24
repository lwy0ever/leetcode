class Solution:
    def magicalString(self, n: int) -> int:
        # 双指针
        if n <= 1:
            return n
        s = [1,2,2]
        curMake = 3
        curCnt = 2
        ans = 1
        while curMake < n:
            x = s[-1] ^ 3   # 使1变2,2变1
            for i in range(s[curCnt]):
                s.append(x)
                curMake += 1
                if x == 1:
                    ans += 1
                if curMake == n:
                    return ans
                #print(s)
            curCnt += 1
        return ans