class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return chr(ord(n) - 1)
        # 比n小的回文数,除非n是10..0 或者 10..01的形式,否则和n的位数应该相同,因为有10..01垫底
        # 对于10..0和10..01的形式,一定是9..9是最终答案,因为差值只有1or2
        if n in ('1' + '0' * (l - 2) + '0','1' + '0' * (l - 2) + '1'):
                return '9' * (l - 1)
        # 类似的,比n大的回文数,除非n是9..9,否则和n的位数应该相同,因为有9..9垫底
        # 对于9..9的形式,一定是10..01是最终答案,因为差值只有2
        if n == '9' * l:
                return '1' + '0' * (l - 1) + '1'
        # 非9..9,10..0和10..01的形式

        # 找比n小的
        # 如果前半段+翻转后的数比n小,就ok了
        # 如果前半段+翻转后的数比n大或者相等,则前半段-1后再翻转
        mid = (l + 1) // 2
        #print(n[:mid] + n[:mid - (l & 1)][::-1])
        if n[:mid] + n[:mid - (l & 1)][::-1] < n:
            ansSmallStr = n[:mid] + n[:mid - (l & 1)][::-1]
        else:
            half = str(int(n[:mid]) - 1)
            if l & 1:   # 奇数长度
                ansSmallStr = half + half[:-1][::-1]
            else:   # 偶数长度
                ansSmallStr = half + half[::-1]
        smallABS = int(n) - int(ansSmallStr)

        # 找比n大的
        # 如果前半段+翻转后的数比n大,就ok了
        # 如果前半段+翻转后的数比n小或者相等,则前半段+1后再翻转
        if n[:mid] + n[:mid - (l & 1)][::-1] > n:
            ansBigStr = ''.join(n[:mid] + n[:mid - (l & 1)][::-1])
        else:
            half = str(int(n[:mid]) + 1)
            if l & 1:   # 奇数长度
                ansBigStr = half + half[:-1][::-1]
            else:   # 偶数长度
                ansBigStr = half + half[::-1]
        bigABS = int(ansBigStr) - int(n)
        
        #print(ansSmallStr,smallABS)
        #print(ansBigStr,bigABS)
        if smallABS <= bigABS:
            return ansSmallStr
        else:
            return ansBigStr
