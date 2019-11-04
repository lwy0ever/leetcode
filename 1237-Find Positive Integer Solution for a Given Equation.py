"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        #print(customfunction.f(1,4))
        ans = []
        y = 1000
        for x in range(1,1001):
            while y > 0:
                t = customfunction.f(x,y)
                if t == z:
                    ans.append([x,y])
                    break
                elif t > z:
                    y -= 1
                else:   # t < z
                    break
        return ans