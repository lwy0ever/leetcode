class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def dfs(arr,a):  # arr表示可用的数组,a表示已经形成的排列
            n = len(arr)
            if n == 0:
                ans.append(a)
                return
            
            for i in range(n):
                if i > 0 and arr[i] == arr[i - 1]:  # 重复元素,跳过
                    continue
                dfs(arr[:i] + arr[i + 1:],a + [arr[i]])
        
        dfs(nums,[])
        return ans