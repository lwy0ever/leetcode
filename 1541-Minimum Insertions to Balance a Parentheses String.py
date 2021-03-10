class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left += 1
                if right & 1:   # 奇数个right
                    ans += 1
                    right += 1  # 加一个right
                while right >= 2 and left > 0:
                    left -= 1
                    right -= 2
                ans += right // 2   # 加right // 2个(
                right = 0
            else:
                right += 1
                if left == 0:
                    ans += 1    # 需要1个left
                    left += 1
                while right >= 2 and left > 0:
                    left -= 1
                    right -= 2
            #print(s[i],ans,left,right)
        if left > 0:
            if right > 0:   # right == 1
                ans += 1
                right += 1
                left -= 1
                right -= 2  # right变0
            ans += left * 2
        else:   # left == 0
            ans += right // 2 + (right & 1) * 2
        return ans