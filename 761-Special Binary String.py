class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        '''
        首先分析一下，如果是满足题目要求的字符串，必然起始字符是"1"，结束字符是"0"
        首先将字符串进行分割，分割成满足条件的子串
        然后针对每个子串，去掉首尾字符后递归
        最后针对已经内部排好序的子串进行排序，并且链接返回
        '''
        
        '''
        例如：11011000
        1、首先进行子串分割，得到：
            [11011000]
	    2、然后去掉首尾字符，得到 101100，递归处理
        3、分割子串 101100，得到
            [10,1100]
            分别继续递归处理，返回值依旧是上面本身
            然后字典序排序，连接返回 
            110010
        4、添加上首尾的1，0
            11100100
        5、由于数组中只有一个元素，排序连接直接返回本身
        '''
        #print(s)
        if len(s) <= 2:
            return s
        
        cnt = 0
        start = 0
        specialStrs = []
        
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                cnt += 1
            if s[i] == '0':
                cnt -= 1
                if cnt == 0:
                    specialStrs.append('1' + self.makeLargestSpecial(s[start + 1:i]) + '0')
                    start = i + 1
        #print(s,specialStrs)

        return ''.join(sorted(specialStrs,reverse = True))