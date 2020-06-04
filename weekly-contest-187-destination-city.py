class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fromP = set()
        for f,t in paths:
            fromP.add(f)
        for f,t in paths:
            if t not in fromP:
                return t