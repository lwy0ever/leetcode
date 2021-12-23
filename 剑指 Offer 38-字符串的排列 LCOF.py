class Solution:
    def permutation(self, s: str) -> List[str]:
        # 已经拼接了pre,剩余可用字符为cnt,剩余总数量为remain
        def helper(pre,cnt,remain):
            for k,v in cnt.items():
                if v == 0:
                    continue
                if remain == 1:
                    ans.append(pre + k)
                else:
                    cnt[k] -= 1
                    helper(pre + k,cnt,remain - 1)
                    cnt[k] += 1

        ans = []
        n = len(s)
        cnt = collections.Counter(s)
                    
        helper('',cnt,n)
        return ans