class Solution:
    def isNumber(self, s: str) -> bool:
        # 状态机
        '''
        state	blank	+/-	0-9	.	e	other
        0   	0   	1	6	2	-1	-1
        1   	-1	    -1	6	2	-1	-1
        2   	-1	    -1	3	-1	-1	-1
        3   	8   	-1	3	-1	4	-1
        4   	-1  	7	5	-1	-1	-1
        5   	8   	-1	5	-1	-1	-1
        6   	8   	-1	6	3	4	-1
        7	    -1  	-1	5	-1	-1	-1
        8	    8   	-1	-1	-1	-1	-1
        '''
        transfer = [[ 0, 1, 6, 2,-1,-1],
                    [-1,-1, 6, 2,-1,-1],
                    [-1,-1, 3,-1,-1,-1],
                    [ 8,-1, 3,-1, 4,-1],
                    [-1, 7, 5,-1,-1,-1],
                    [ 8,-1, 5,-1,-1,-1],
                    [ 8,-1, 6, 3, 4,-1],
                    [-1,-1, 5,-1,-1,-1],
                    [ 8,-1,-1,-1,-1,-1]]
        finals = [0,0,0,1,0,1,1,0,1]
        stat = 0
        for c in s:
            if c == ' ':
                t = 0
            elif c in ('+','-'):
                t = 1
            elif ord('0') <= ord(c) <= ord('9'):
                t = 2
            elif c == '.':
                t = 3
            elif c == 'e':
                t = 4
            else:
                t = 5
            #print(stat,t)
            stat = transfer[stat][t]
            if stat == -1:
                return False
        return finals[stat]
                
        