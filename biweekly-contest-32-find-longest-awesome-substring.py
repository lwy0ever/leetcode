class Solution:
    def longestAwesome(self, s: str) -> int:
        # 使用二进制方式记录状态
        status = {0:-1} # 记录状态最早出现的位置
        st = 0
        ans = 1
        for i,c in enumerate(s):
            st ^= (1 << int(c))
            if st in status:    # 状态st出现过
                ans = max(ans,i - status[st])   # abccba回文模式
            else:   # 状态st没有出现过
                status[st] = i
            for x in range(10): # abcba回文模式
                ns = st ^ (1 << x)
                if ns in status:
                    ans = max(ans,i - status[ns])
        return ans