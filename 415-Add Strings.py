class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        n1 = len(num1)
        n2 = len(num2)
        # 保证n1 >= n2,从而可以将结果直接存放在1中,并且不用做过多判断
        if n1 < n2:
            num1,num2 = num2,num1
            n1,n2 = n2,n1
        s1 = [int(x) for x in num1]
        s2 = [int(x) for x in num2]
        # 倒序存储,便于将来处理进位
        s1 = s1[::-1]
        s2 = s2[::-1]
        for i in range(n2):
            s1[i] += s2[i]
        
        def CarrySolver(arr):
            i = 0
            while i < len(arr):
                if arr[i] >= 10:
                    ad = arr[i] // 10
                    if i + 1 == len(arr):
                        arr.append(ad)
                    else:
                        arr[i + 1] += ad
                    arr[i] %= 10
                i += 1
            return arr
        
        ans = ''.join([str(x) for x in CarrySolver(s1)][::-1])
        return ans

        '''
        ans = []
        ad = 0
        n1 = len(num1)
        n2 = len(num2)
        for i in range(max(n1,n2)):
            a = int(num1[-i-1] if i < n1 else 0)
            b = int(num2[-i-1] if i < n2 else 0)
            t = a + b + ad
            ad,m = divmod(t,10)
            ans.append(m)
        while ad > 0:
            ad,m = divmod(ad,10)
            ans.append(m)
        ans.reverse()
        return ''.join(map(str,ans))
        '''