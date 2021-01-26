class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 最终简化
        d,m = divmod(k - n,25)
        if m == 0:
            return 'a' * (n - d) + 'z' * d
        else:
            return 'a' * (n - d - 1) + chr(ord('a') + m) + 'z' * d

        # 每个字符,最小是a,最大是z
        # 前面的字符尽可能选择a
        '''
        # 'a' * a + '?' + 'z' * z = k
        # 二元一次方程
        # 1 * a + '?' + 26 * z = k
        # a + 1 + z = n
        # => 25 * z + '?' - 1 = k - n
        d,m = divmod(k - n + 1,25)
        #print(d,m)
        # '?'是y时,m = 0,z = d - 1
        # '?'是z时,m = 1,z = d - 2
        # '?'是b - x时,z = d
        # '?'是a时,m = 1,25 * z + 1 = k - n + 1
        a = 0
        if m == 0:
            z = d - 1
            ch = 'y'
        elif m == 1:
            if (k - n) % 25 == 0:
                z = (k - n) // 25
                ch = ''
                a += 1
            else:
                z = d - 2
                ch = 'z'
        else:
            z = d
            ch = chr(ord('a') + m - 1)
        a += n - z - 1
        return 'a' * a + ch + 'z' * z
        '''
        
        # 每个字符,最小是a,最大是z
        # 前面的字符尽可能选择a
        '''
        ans = ''
        for i in range(n):
            #print(26 * (n - i - 1),k)
            if 26 * (n - i - 1) + 1 >= k:
                ans += 'a'
                k -= 1
            elif 26 * (n - i - 1) == k:
                ans += 'z' * (n - i - 1)
                break
            else:
                ans += chr(ord('a') + k - 26 * (n - i - 1) - 1)
                k = 26 * (n - i - 1)
            #print(ans)
        return ans
        '''