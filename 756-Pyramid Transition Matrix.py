from collections import defaultdict
class Solution:
    def ppt(self,bottom,al):
        TOPs = []   # 新底部
        for i in range(len(bottom) - 1):
            LR = bottom[i:i + 2]    # 底部2块block
            Ts = [] # 底部2块block可能组成的block
            if LR in al:
                for t in al[LR]:
                    Ts.append(t)
            if not Ts:
                return False
            if not TOPs:
                TOPs = Ts
            else:
                TTT = []
                for t in TOPs:
                    for b in Ts:
                        TTT.append(t + b)   # 连接已经形成的底部和新的block
                TOPs = TTT
        #print(TOPs)

        for t in TOPs:
            if len(t) == 1:
                return True
            if self.ppt(t,al):   # 递归新底部
                return True

        return False

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        al = defaultdict(list)
        for a,b,c in allowed:
            al[a + b].append(c)
        #print(al)
        return self.ppt(bottom,al)
