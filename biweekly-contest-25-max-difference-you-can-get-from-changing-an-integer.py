class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)
        # get a
        arr = []
        x = 'X'
        for i in range(n):
            if s[i] != '9':
                if x == 'X':
                    x = s[i]
                    arr.append('9')
                elif x == s[i]:
                    arr.append('9')
                else:
                    arr.append(s[i])
            else:
                arr.append(s[i])
        #print(arr)
        a = int(''.join(arr))
        # get b
        arr = []
        x = 'X'
        if s[0] != '1':
            arr.append('1')
            x = s[0]
            y = '1'
        else:
            arr.append(s[0])
        for i in range(1,n):
            if s[i] != '0':
                if x == 'X' and s[i] != '1':
                    x = s[i]
                    y = '0'
                    arr.append('0')
                elif x == s[i]:
                    arr.append(y)
                else:
                    arr.append(s[i])
            else:
                arr.append(s[i])
        #print(arr)
        b = int(''.join(arr))
        return a - b
                
            
                