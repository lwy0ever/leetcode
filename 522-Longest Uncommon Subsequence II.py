class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # key:如果strs[i]的某个子序列是 独有的子序列,那么strs[i]一定也是 独有的子序列
        # 所以,只需要判断strs[i]是不是独有子序列即可

        # 对于strA和strB,判断A是否是B的独有子序列,使用双指针+贪心
        def isSub(a,b):
            na = len(a)
            nb = len(b)
            ia = 0
            ib = 0
            while ia < na and ib < nb:
                if a[ia] == b[ib]:
                    ia += 1
                ib += 1
            if ia == na:    # 检查到了a的结尾,成功
                return True
            else:
                return False

        ans = -1
        n = len(strs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isSub(strs[i],strs[j]):
                    break
            else:
                ans = max(ans,len(strs[i]))
        return ans