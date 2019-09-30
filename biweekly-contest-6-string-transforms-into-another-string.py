from collections import Counter
from collections import defaultdict

class Solution:
        
    def canConvert(self, str1: str, str2: str) -> bool:
        n = len(str1)
        cp1 = defaultdict(list)
        #cp2 = defaultdict(set)
        for i in range(n):
            cp1[str1[i]].append(i)
            #cp2[str2[i]].add(i)
        if len(Counter(str2)) == 26 and str1 != str2:
            return False
        for k in cp1.keys():
            pre = str2[cp1[k][0]]
            for p in cp1[k]:
                if str2[p] != pre:
                    return False
        return True
        
