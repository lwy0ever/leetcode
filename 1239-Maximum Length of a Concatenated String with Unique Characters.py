class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        setarr = []
        for s in arr:
            st = set()
            for c in s:
                if c in st:
                    break
                else:
                    st.add(c)
            else:
                setarr.append(st)
        #print(setarr)
        n = len(setarr)
        for i in range(2 ** n):
            st = set()
            for m in range(n):
                if i & (1 << m) > 0:
                    if not st.isdisjoint(setarr[m]):
                        break
                    st = st.union(setarr[m])
                    #print(i,m,i & (1 << m),st)
            ans = max(ans,len(st))
        return ans