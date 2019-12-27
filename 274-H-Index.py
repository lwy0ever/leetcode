class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 计数法
        n = len(citations)
        paper = [0] * (n + 1)   # 记录分值为i的文章的引用次数,由于h-index无法超过论文的篇数n,所以分值超过n的时候,仍然记为n
        for c in citations:
            paper[min(n,c)] += 1
        s = 0
        i = n
        while i >= 0:
            s += paper[i]
            if s >= i:
                return i
            i -= 1
        '''
        # 排序法
        n = len(citations)
        citations.sort()
        i = 0
        while i < n and citations[- 1 - i] > i:
            i += 1
        return i            
        '''
        '''
        n = len(citations)
        if n == 0:
            return 0
        citations.sort()
        #print(citations)
        if citations[0] >= n:
            return n
        for h in range(n - 1,0,-1):
            #print(h,citations[-h],citations[n - h])
            if citations[-h] >= h and citations[n - 1 - h] <= h:
                return h
        return 0
        '''