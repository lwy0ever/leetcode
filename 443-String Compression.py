class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = 0    # 当前相同字符串的起始位置
        write = 0   # 修改后的字符串的结尾位置+1
        for i,char in enumerate(chars):
            if i + 1 == n or char != chars[i + 1]:
                chars[write] = chars[read]
                write += 1
                cnt = i + 1 - read
                if cnt > 1:
                    chars[write:write + len(str(cnt))] = str(cnt)
                    write += len(str(cnt))
                read = i + 1
        return write
        '''
        ans = 0
        pre = chars[0]
        cnt = 1
        ind = 0
        for c in chars[1:]:
            if c == pre:
                cnt += 1
            else:
                if cnt == 1:
                    ans += 1
                    chars[ind] = pre
                else:
                    ans += 1 + len(str(cnt))
                    chars[ind:ans] = pre + str(cnt)
                ind = ans
                pre = c
                cnt = 1
            #print(c,ind,ans,chars)
        if cnt == 1:
            ans += 1
            chars[ind] = pre
        else:
            ans += 1 + len(str(cnt))
            chars[ind:ans] = pre + str(cnt)
        #print(ans)
        return ans
        '''