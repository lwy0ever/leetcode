class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        origin = set(wordlist)
        lowerChanged = dict()
        vowelChanged = dict()
        vowel = {'a','e','i','o','u'}
        
        def changeVowel(s):
            return ''.join(['*' if c in vowel else c for c in s])
        
        for w in wordlist:
            l = w.lower()
            lowerChanged.setdefault(l,w)
            vc = changeVowel(l)
            vowelChanged.setdefault(vc,w)
        #print(lowerChanged)
        #print(vowelChanged)
        
        ans = []
        for q in queries:
            if q in origin:
                ans.append(q)
                continue
            l = q.lower()
            if l in lowerChanged:
                ans.append(lowerChanged[l])
                continue
            vc = changeVowel(l)
            if vc in vowelChanged:
                ans.append(vowelChanged[vc])
                continue
            ans.append('')
        return ans