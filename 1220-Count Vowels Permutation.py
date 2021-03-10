class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # a -> e
        # e -> a,i
        # i -> a,e,o,u
        # o -> i,u
        # u -> a
        d = {'a':1,'e':1,'i':1,'o':1,'u':1}
        for i in range(1,n):
            nd = {}
            nd['a'] = d['e'] + d['i'] + d['u']
            nd['e'] = d['a'] + d['i']
            nd['i'] = d['e'] + d['o']
            nd['o'] = d['i']
            nd['u'] = d['i'] + d['o']
            d = nd
        return sum(d.values()) % (10 ** 9 + 7)