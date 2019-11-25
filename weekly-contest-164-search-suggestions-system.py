class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l = 0
        r = len(products)
        n = len(searchWord)
        ans = []
        for i in range(n):
            wd = searchWord[:i + 1]
            nl = bisect.bisect_left(products,wd,l,r)
            nr = bisect.bisect_left(products,wd + 'z' * n,l,r)
            #print(nl,nr,products[nl:nr])
            ans.append(products[nl:nr][:3])
        return ans
