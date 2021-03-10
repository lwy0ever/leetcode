class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # 并查
        # l[i]表示以i为边界的连续的1的长度(包括向左和向右),由于连续1中间的数字无意义(不需要再被考虑,所以不需要更新)
        # cnt[i]表示长度为i的连续1的子串数量
        n = len(arr)
        l = [0] * (n + 2)
        cnt = [0] * (n + 1)
        # 每一步,都使l[arr[i] - 1]和l[arr[i] + 1]被连接起来
        # 新长度newLen = l[arr[i] - 1] + l[arr[i] + 1] + 1
        # 于是,l[arr[i] - l[arr[i] - 1]] = newLen,l[arr[i] + l[arr[i] + 1]] = newLen
        # cnt[l[arr[i] - 1]] -= 1,cnt[l[arr[i] + 1]] -= 1
        # cnt[newLen] += 1
        ans = -1
        for i in range(n):
            left = l[arr[i] - 1]
            right = l[arr[i] + 1]
            newLen = left + right + 1
            l[arr[i] - left] = l[arr[i] + right] = newLen
            cnt[left] -= 1
            cnt[right] -= 1
            cnt[newLen] += 1
            if cnt[m] > 0:  # 还有满足条件的,则记录下来
                ans = i + 1
            #print(left,right,l,cnt,ans)
        return ans
        
        '''
        # 二分法,O(NlogN)
        # 反过来想
        # 原来是一个全1的二进制字符串,将arr[::-1]的位置依次变为0
        # 用二分查找,左右设置哨兵
        n = len(arr)
        if m == n:
            return n
        bits = [0,n + 1]
        for i in range(1,n + 1):
            p = bisect.bisect_left(bits,arr[-i])
            #print(bits,arr[-i],p)
            bisect.insort_left(bits,arr[-i])
            #print(bits,p)
            if bits[p] - bits[p - 1] == m + 1 or bits[p + 1] - bits[p] == m + 1:
                return n - i
        return -1
        '''