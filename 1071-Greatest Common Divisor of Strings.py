class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # T必然是str1[:i],也就是必然位于一个字符串的开始部分
        n1 = len(str1)
        n2 = len(str2)
        if n1 > n2:
            str1,str2 = str2,str1
            n1,n2 = n2,n1
        for i in range(n1,0,-1):
            l = len(str1[:i])
            if n1 % l == 0 and n2 % l == 0:
                if str1[:i] * (n1 // l) == str1 and str1[:i] * (n2 // l) == str2:
                    return str1[:i]
        return ''