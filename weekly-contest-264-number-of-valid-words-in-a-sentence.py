class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        # 0表示开始
        # 1表示在-之前出现了字母
        # 2表示出现了-
        # 3表示在-之后出现了字母
        # 4表示出现了标点符号
        # -1表示出现过数字,或者多个-,或者多个标点符号
        stat = 0
        for c in sentence:
            if ord('a') <= ord(c) <= ord('z'):
                if stat in (0,1):
                    stat = 1
                elif stat in (2,3):
                    stat = 3
                else:
                    stat = -1
            elif ord('0') <= ord(c) <= ord('9'):
                stat = -1
            elif c == '-':
                if stat in (0,2,3,4):
                    stat = -1
                elif stat == 1:
                    stat = 2
            elif c in ('!','.',','):
                if stat in (0,1,3):
                    stat = 4
                else:
                    stat = -1
            else:   # c == ' '
                if stat in (1,3,4):
                    ans += 1
                stat = 0
            #print(c,ans,stat)
        if stat in (1,3,4):
            ans += 1
        #print(ans,stat)
        return ans
                