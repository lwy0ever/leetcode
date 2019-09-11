class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        arr = []
        def contrib(pre,n,length):
            if n == length:
                arr.append(pre + 2 ** n - 1)
                return
            if n > 0:
                contrib(pre + 0,n,length - 1)
                contrib(pre + (1 << (length - 1)),n - 1,length - 1)
            else:
                arr.append(pre)
        
        ans = []
        if num > 10:
            return ans
        contrib(0,num,10)
        #print(arr)
        for a in arr:
            h = a >> 6
            m = a - (h << 6)
            #print(h,m)
            if h < 12 and m < 60:
                ans.append('%d:%02d'%(h,m))
        return ans