class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 类似bfs
        m = len(nums)
        fromP = [(0,0)]
        ans = []
        ans.append(nums[0][0])
        while fromP:
            newP = []
            for x,y in fromP:
                for tx,ty in (x + 1,y),(x,y + 1):
                    if tx < m and ty < len(nums[tx]) and nums[tx][ty] != -1:
                        ans.append(nums[tx][ty])
                        newP.append((tx,ty))
                        nums[tx][ty] = -1   # -1表示访问过
            fromP = newP
        return ans
                    