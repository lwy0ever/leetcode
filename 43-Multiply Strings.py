class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 竖式优化,逐位相乘,整体相加
        # 比如34 * 56
        #     34
        #   x 56
        # ------
        #     24
        #    18
        #    20
        #   15
        # ------
        #   1904
        # toadd[i]表示需要左移i位的结果
        # 例如上例中的3x5,在toadd[2]里面
        # 最多移动len(num1) + len(num2) - 2位
        if num1 == '0' or num2 == '0':
            return '0'

        def multi(num,n):
            toadd = []
            n = int(n)
            for x in num[::-1]:
                toadd.append(int(x) * n)
            toadd = CarrySolver(toadd)
            return ''.join(str(x) for x in toadd[::-1])

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

        def addStrings(num1, num2):
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
            ans = ''.join([str(x) for x in CarrySolver(s1)][::-1])
            return ans

        ans = '0'
        for i,n in enumerate(num2[::-1]):
            tmp = multi(num1,n)
            ans = addStrings(ans,tmp + '0' * i)
        return ans
