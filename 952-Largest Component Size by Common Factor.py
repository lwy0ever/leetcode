class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def lcd(x,y):   #求最大公约数
            d,m = divmod(x,y)
            if m == 0:
                return y
            return lcd(y,m)
        
        prime = [2]
        mm = max(A)
        for i in range(3,int(mm ** 0.5) + 1,2):
            for p in prime:
                if p * p > i:
                    prime.append(i)
                    break
                if lcd(i,p) > 1:
                    break
            else:
                prime.append(i)
        #print(prime)
        n = len(A)
        pn = len(prime)
        #pset = set(prime)
        pset = set()
        #prime_A = collections.defaultdict(set)
        A_prime = collections.defaultdict(list)
        for i,a in enumerate(A):
            t = a
            for p in prime:
                if t % p == 0:
                    pset.add(p)
                    #prime_A[p].add(a)
                    A_prime[a].append(p)
                    while t % p == 0:
                        t //= p
            if t > 1:
                pset.add(t)
                A_prime[a].append(t)
        #print(A_prime)

        prime = list(pset)
        prime_index = {p:i for i,p in enumerate(prime)} #表示质数的位置
        group = [i for i in range(len(prime))]   #表示质数的分组情况
        #print(prime)
        #print(prime_index)
        
        def Gfind(x):    #找到元素x的分组情况
            if group[x] != x:
                group[x] = Gfind(group[x])
            return group[x]

        def Gunion(x,y):    #合并x、y的分组
            fx = Gfind(x)
            fy = Gfind(y)
            group[fy] = fx
        
        for pr in A_prime.values():
            fa = pr[0]
            for p in pr:
                Gunion(prime_index[fa],prime_index[p])
        #print(group)
        cnt = collections.Counter([Gfind(prime_index[pr[0]]) for pr in A_prime.values()])
        #print(cnt)
        return max(cnt.values())
        '''
        ans = 0
        while pset:
            used = set()
            aed = set()
            p = pset.pop()
            used.add(p)
            toConnectPrime = {p}
            cnt = 0
            while toConnectPrime:
                p = toConnectPrime.pop()
                used.add(p)
                if p in pset:
                    pset.remove(p)
                for a in prime_A[p]:
                    aed.add(a)
                    for p in A_prime[a]:
                        if p not in used:
                            toConnectPrime.add(p)
            ans = max(ans,len(aed))
            #print(aed)
        return ans
        '''
