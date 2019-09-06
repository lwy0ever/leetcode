class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        #print(pairs)
        end = float('-inf')
        ans = 0
        for a,b in pairs:
            if a > end:
                ans += 1
                end = b
        return ans