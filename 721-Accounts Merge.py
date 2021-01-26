class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 并查集
        email_index = dict()
        email_account = dict()
        ind = 0
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e not in email_index:
                    email_index[e] = ind
                    email_account[e] = a[0]
                    ind += 1
        
        parent = list(range(ind))
        
        def findparent(i):
            if parent[i] != i:
                parent[i] = findparent(parent[i])
            return parent[i]
        
        def union(a,b):
            parent[findparent(b)] = findparent(a)
        
        for a in accounts:
            firstIndex = email_index[a[1]]
            for e in a[2:]:
                union(firstIndex,email_index[e])
        
        index_email = collections.defaultdict(list)
        for email,ind in email_index.items():
            index_email[findparent(ind)].append(email)

        ans = []
        for ind,email in index_email.items():
            ans.append([email_account[email[0]]] + sorted(email))
        return ans