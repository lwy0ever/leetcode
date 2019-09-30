# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        l = 6
        wl = set(wordlist)
        while wl:
            w = wl.pop()
            n = master.guess(w)
            if n == l:
                return
            nl = set()
            for e in wl:
                c = 0
                for i in range(l):
                    if e[i] == w[i]:
                        c += 1
                if c == n:
                    nl.add(e)
            #print(w,n,nl)
            wl = nl
            
        