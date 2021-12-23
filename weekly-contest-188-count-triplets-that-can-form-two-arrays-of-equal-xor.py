class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # O(n)
        # 没想明白
        cnt = Counter()
        total = Counter()
        p = 0
        ans = 0
        for k, val in enumerate(arr):
            if (t := p ^ val) in cnt:
                ans += cnt[t] * k - total[t]
            cnt[p] += 1
            total[p] += k
            p = t
        return ans

        # O(n ^ 2)
        p = 0
        pre = [p]
        for a in arr:
            p ^= a
            pre.append(p)
        #print(pre)
        n = len(arr)
        ans = 0
        for i in range(n):
            for k in range(i + 1,n):
                # a == b,也就是arr[i] ^ ... arr[k] == 0
                if pre[k + 1] == pre[i]:
                    ans += k - i
        return ans

        # O(n ^ 3)
        p = 0
        pre = [p]
        for a in arr:
            p ^= a
            pre.append(p)
        #print(pre)
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j,n):
                    # a == b,也就是arr[i] ^ ... arr[k] == 0
                    if pre[k + 1] == pre[i]:
                        ans += 1
                        #print(i,j,k)
        return ans