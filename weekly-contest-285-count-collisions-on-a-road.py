class Solution:
    def countCollisions(self, directions: str) -> int:
        # 左侧的L不会相撞
        # 右侧的R不会相撞
        # 中间的除了S,都会相撞
        n = len(directions)
        l = 0
        r = n - 1
        while l < n and directions[l] == 'L':
            l += 1
        while r >= 0 and directions[r] == 'R':
            r -= 1
        Scnt = 0
        for i in range(l,r + 1):
            if directions[i] == 'S':
                Scnt += 1
        return r + 1 - l - Scnt
        
        '''
        pre = 'L'
        ans = 0
        rCnt = 0
        for c in directions:
            #print(pre,c,ans)
            if pre == 'L':
                pre = c
                if c == 'R':
                    rCnt = 1
            elif pre == 'S':
                if c == 'L':
                    pre = 'S'
                    ans += 1
                elif c == 'R':
                    pre = 'R'
                    rCnt = 1
            else:   # pre == 'R'
                if c == 'L':
                    ans += 1 + rCnt
                    pre = 'S'
                elif c == 'S':
                    ans += rCnt
                    pre = 'S'
                else:   # c == 'R'
                    rCnt += 1
        return ans
        '''