class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 二分法
        # 答案一定在matrix[0][0]到matrix[-1][-1]的范围内
        
        # 由于每行\每列都是升序排列,所以可以用最多n * 2次,统计出小于等于某个数字的数量
        # 从左下角matrix[-1][0]开始
        # 如果目标大于当前值,则右移
        # 如果目标小于等于当前值,则上移
        def count(target):
            i,j = n - 1,0
            cnt = 0 # 统计小于等于target的数量
            while i >= 0 and j < n:
                if target >= matrix[i][j]:
                    cnt += i + 1    # 从0到i行,第j列都小于等于target
                    j += 1
                else:
                    i -= 1
            return cnt
        
        n = len(matrix)
        l,r = matrix[0][0],matrix[-1][-1]
        while l < r:
            m = (l + r) // 2
            cnt = count(m)
            if cnt >= k:
                r = m
            else:   # 不足k个
                l = m + 1
        return l
        
        # 类归并法
        '''
        n = len(matrix)
        cur = [0] * n   # n个指针,记录每行的当前指针位置
        val = []    # 记录当前n个指针指向的值,已排序
        valPos = [] # 记录当前n个指针指向的值所在的行,已按照值排序
        for i in range(n):
            pos = bisect.bisect(val,matrix[i][0])
            valPos.insert(pos,i)
            val.insert(pos,matrix[i][0])
        ans = 0
        for _ in range(k):
            ans = val.pop(0)
            row = valPos.pop(0)
            cur[row] += 1
            if cur[row] < n:
                pos = bisect.bisect(val,matrix[row][cur[row]])
                valPos.insert(pos,row)
                val.insert(pos,matrix[row][cur[row]])
        return ans
        '''