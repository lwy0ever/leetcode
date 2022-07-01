class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 利用双指针
        # 先从前到后,找到最后一个留下的数字
        # 再从后到前,修改元素
        n = len(arr)
        l = 0
        r = 0
        while r < n:
            if arr[l] == 0:
                r += 1
            l += 1
            r += 1
            #print(l,r)
        if r == n + 1:  # 说明最后留下的数字是0,但是没有空间用来复制
            l -= 1
            r -= 2
            arr[r] = arr[l]
        #print(l,r,arr)
        while l > 0:
            l -= 1
            r -= 1
            arr[r] = arr[l]
            if arr[l] == 0:
                r -= 1
                arr[r] = arr[l]
            #print(l,r,arr)