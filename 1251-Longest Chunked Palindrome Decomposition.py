class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        #if n == 1:
        #    return 1
        l = 0
        r = n
        length = 1
        cnt = n
        while l + length <= n // 2:
            #print(l,r,length)
            #print(text[l:l + length],text[r - length:r],cnt)
            if text[l:l + length] == text[r - length:r]:
                l += length
                r -= length
                length = 1
            else:
                length += 1
                cnt -= 2
        if text[l:l + length - 1] != text[r - length + 1:r] and n % 2 == 0:
            cnt += 1
        return cnt