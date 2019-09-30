class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        An = len(A)
        Bn = len(B)
        
        # 返回值:
        # return[0]:
        #    -1表示a[1] > b[1]
        #    0 表示a[1] == b[1]
        #    1 表示a[1] < b[1]
        # return[1]:a和b的交集
        def intersection(a,b):
            if b[1] < a[0]:
                return -1,[]
            if b[1] < a[1]: # and b[1] >= a[0]
                return -1,[max(a[0],b[0]),b[1]]
            if b[1] == a[1]:
                return 0,[max(a[0],b[0]),b[1]]
            if b[0] <= a[1]: # and b[1] > a[1]
                return 1,[max(a[0],b[0]),a[1]]
            if b[0] > a[1]: # and b[1] > a[1]
                return 1,[]
        
        i = j = 0
        ans = []
        while i < An and j < Bn:
            t,inte = intersection(A[i],B[j])
            if t == -1:
                j += 1
            elif t == 1:
                i += 1
            else:
                i += 1
                j += 1
            if inte:
                ans.append(inte)
        return ans
            
        