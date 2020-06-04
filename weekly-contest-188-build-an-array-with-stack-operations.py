class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        cur = 1
        for t in target:
            while cur < t:
                ans.append('Push')
                ans.append('Pop')
                cur += 1
            ans.append('Push')
            cur += 1
        return ans