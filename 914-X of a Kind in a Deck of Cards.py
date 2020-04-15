class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        from functools import reduce
        from collections import Counter
        cnt = Counter(deck)
        return reduce(gcd,cnt.values()) >= 2
        '''
        cnt = collections.Counter(deck)
        _min = min(cnt.values())
        for i in range(2,_min + 1):
            for v in cnt.values():
                if v % i != 0:
                    break
            else:
                return True
        return False
        '''